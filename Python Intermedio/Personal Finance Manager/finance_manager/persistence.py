"""
Student: Cesar Lanuza Urbina
Program: Load validated JSON state and save it atomically without destroying invalid files.
"""

import json
import os
import tempfile
from datetime import date
from pathlib import Path

from .errors import PersistenceError, ValidationError
from .models import Category, FinanceState, Transaction
from .validation import validate_color, validate_date, validate_amount, validate_text


class FinanceRepository:
    """Own JSON serialization and validate data before exposing it to services."""

    def __init__(self, path, today=None):
        """Configure a data path and an injectable date provider for tests."""
        self.path = Path(path).resolve()
        self.today = today or date.today
        self._blocked = False

    def load(self):
        """Return an empty state for a missing file; never repair corrupt data silently."""
        if self._blocked:
            raise PersistenceError("La carga está bloqueada por un error anterior; revise el archivo y reinicie.")
        try:
            with self.path.open("r", encoding="utf-8") as file:
                raw = json.load(file)
            return self._decode(raw)
        except FileNotFoundError:
            return FinanceState()
        except (OSError, UnicodeError, ValueError, TypeError, KeyError, ValidationError) as error:
            self._blocked = True
            raise PersistenceError(
                f"No se pudo cargar {self.path}. El archivo no se modificó. "
                "Revise sus permisos o restaure una copia válida antes de reiniciar."
            ) from error

    def _decode(self, raw):
        """Validate schema, identities, references, and all stored field values."""
        if not isinstance(raw, dict) or type(raw.get("version")) is not int or raw["version"] != 1:
            raise ValueError("Versión de datos no compatible.")
        categories_raw, movements_raw = raw["categorias"], raw["movimientos"]
        if not isinstance(categories_raw, list) or not isinstance(movements_raw, list):
            raise ValueError("Las categorías y los movimientos deben ser listas.")
        categories, movements = [], []
        ids, names = set(), set()
        for item in categories_raw:
            category = Category(
                validate_text(item["id"], "identificador"),
                validate_text(item["nombre"], "nombre", 60),
                validate_color(item["color"]),
            )
            if category.id in ids or category.nombre.casefold() in names:
                raise ValueError("Hay categorías duplicadas.")
            ids.add(category.id)
            names.add(category.nombre.casefold())
            categories.append(category)
        movement_ids = set()
        for item in movements_raw:
            raw_date = item["fecha"]
            if not isinstance(raw_date, str):
                raise ValueError("Fecha de datos inválida.")
            parsed = date.fromisoformat(raw_date)
            if raw_date != parsed.isoformat():
                raise ValueError("Formato de fecha de datos inválido.")
            validated_date = validate_date(parsed.strftime("%d/%m/%Y"), self.today())
            movement = Transaction(
                validate_text(item["id"], "identificador"), validated_date,
                validate_text(item["titulo"], "título"), validate_amount(item["monto"]),
                item["categoria_id"], item["tipo"],
            )
            if (movement.id in movement_ids or movement.categoria_id not in ids
                    or movement.tipo not in ("Ingreso", "Gasto")):
                raise ValueError("El movimiento contiene referencias o tipo inválidos.")
            movement_ids.add(movement.id)
            movements.append(movement)
        return FinanceState(tuple(categories), tuple(movements))

    # 
    def save(self, state):
        """Flush a temporary file and replace the destination only after a successful write."""
        if self._blocked:
            raise PersistenceError("El guardado está bloqueado para proteger el archivo que no pudo cargarse.")
        raw = {
            "version": 1,
            "categorias": [{"id": c.id, "nombre": c.nombre, "color": c.color} for c in state.categories],
            "movimientos": [{
                "id": m.id, "fecha": m.fecha.isoformat(), "titulo": m.titulo,
                "monto": str(m.monto), "categoria_id": m.categoria_id, "tipo": m.tipo,
            } for m in state.transactions],
        }
        temporary = None
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=self.path.parent,
                                             prefix=".finanzas-", suffix=".tmp", delete=False) as file:
                temporary = Path(file.name)
                json.dump(raw, file, ensure_ascii=False, indent=2)
                file.flush()
                os.fsync(file.fileno())
            os.replace(temporary, self.path)
        except (OSError, UnicodeError) as error:
            raise PersistenceError("No se pudieron guardar los cambios. Revise permisos y espacio disponible; no se aplicó la operación.") from error
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)