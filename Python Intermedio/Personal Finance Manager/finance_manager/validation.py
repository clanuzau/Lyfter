"""
Student: Cesar Lanuza Urbina
Program: Validate titles, dates, positive monetary amounts, and category colors.
"""

import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

from .errors import ValidationError

MAX_AMOUNT = Decimal("999999999999.99")


def validate_text(value, field, maximum=100):
    """Normalize visible text and reject empty or multiline input."""
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"El campo {field} es obligatorio.")
    text = value.strip()
    if len(text) > maximum or any(ord(char) < 32 for char in text):
        raise ValidationError(f"El campo {field} admite hasta {maximum} caracteres sin saltos de línea.")
    return text


def validate_color(value):
    """Accept a six-digit hexadecimal color and normalize it to uppercase."""
    if not isinstance(value, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise ValidationError("El color debe usar el formato #RRGGBB, por ejemplo #DDEEFF.")
    return value.upper()


def validate_amount(value):
    """Accept a positive amount with at most two decimal places."""
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValidationError("El monto debe ser un número mayor que cero.")
    text = str(value).strip().replace(",", ".")
    if not re.fullmatch(r"\d+(?:\.\d{1,2})?", text):
        raise ValidationError("Ingrese un monto positivo con hasta dos decimales, sin separadores de miles.")
    try:
        amount = Decimal(text)
        if not amount.is_finite() or not 0 < amount <= MAX_AMOUNT:
            raise ValidationError("El monto debe ser mayor que cero y no superar 999999999999.99.")
        return amount.quantize(Decimal("0.01"))
    except InvalidOperation as error:
        raise ValidationError("El monto ingresado no es válido.") from error


def validate_date(value, today=None, allow_future=False):
    """Parse a strict dd/mm/yyyy date and reject future transaction dates."""
    if not isinstance(value, str) or not re.fullmatch(r"\d{2}/\d{2}/\d{4}", value):
        raise ValidationError("La fecha debe tener el formato dd/mm/aaaa.")
    try:
        parsed = datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError as error:
        raise ValidationError("La fecha indicada no existe.") from error
    if not allow_future and parsed > (today or date.today()):
        raise ValidationError("La fecha del movimiento no puede ser futura.")
    return parsed


def validate_date_range(start, end):
    """Validate inclusive bounds; future filter bounds are allowed."""
    first = validate_date(start, allow_future=True)
    last = validate_date(end, allow_future=True)
    if first > last:
        raise ValidationError("La fecha inicial no puede ser posterior a la fecha final.")
    return first, last