"""
Student: Cesar Lanuza Urbina
Program: Export all finance records and exact totals to an Excel-friendly CSV file.
"""

import csv
import os
import tempfile
from pathlib import Path

from .errors import ExportError


def escape_spreadsheet_text(value):
    """Escape spreadsheet formulas in user-provided text cells."""
    if value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


class CSVExporter:
    """Write a complete export without touching an existing file on write failure."""

    def export(self, path, movements, categories, totals):
        """Export signed amounts, category names, and income/expense/balance totals."""
        destination = Path(path).resolve()
        category_names = {c.id: c.nombre for c in categories}
        temporary = None
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8-sig", newline="",
                                             dir=destination.parent, prefix=".export-",
                                             suffix=".tmp", delete=False) as file:
                temporary = Path(file.name)
                writer = csv.writer(file)
                writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])
                for movement in movements:
                    writer.writerow([
                        movement.fecha.strftime("%d/%m/%Y"), escape_spreadsheet_text(movement.titulo),
                        f"{movement.signed_amount:.2f}", escape_spreadsheet_text(category_names[movement.categoria_id]),
                        movement.tipo,
                    ])
                writer.writerow([])
                for label, amount in (("Total ingresos", totals.ingresos),
                                      ("Total gastos", totals.gastos), ("Balance", totals.balance)):
                    writer.writerow(["", label, f"{amount:.2f}", "", "Resumen"])
                file.flush()
                os.fsync(file.fileno())
            os.replace(temporary, destination)
            return destination
        except (OSError, UnicodeError) as error:
            raise ExportError("No se pudo exportar el CSV. Revise la ubicación, los permisos y si el archivo está abierto.") from error
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)