"""
Student: Cesar Lanuza Urbina
Program: Define immutable categories, transactions, finance state, and totals.
"""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Category:
    """Store a stable category identity and its display settings."""
    id: str
    nombre: str
    color: str


@dataclass(frozen=True)
class Transaction:
    """Store a positive amount; the transaction type determines its sign."""
    id: str
    fecha: date
    titulo: str
    monto: Decimal
    categoria_id: str
    tipo: str

    @property
    def signed_amount(self):
        """Return a negative expense or a positive income for presentation."""
        return -self.monto if self.tipo == "Gasto" else self.monto


@dataclass(frozen=True)
class FinanceState:
    """Hold a complete immutable snapshot for atomic persistence."""
    categories: tuple[Category, ...] = ()
    transactions: tuple[Transaction, ...] = ()


@dataclass(frozen=True)
class Totals:
    """Expose income, absolute expenses, and the resulting balance."""
    ingresos: Decimal
    gastos: Decimal

    @property
    def balance(self):
        """Subtract absolute expenses from income using Decimal arithmetic."""
        return self.ingresos - self.gastos