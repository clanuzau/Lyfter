"""
Student: Cesar Lanuza Urbina
Program: Build and visually render a professional Spanish user guide with real application screenshots.
"""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from PIL import Image
from pypdf import PdfReader
import pymupdf

ROOT = Path(__file__).resolve().parent
PROJECT = Path(r"C:\Lyfter\Python Intermedio\Personal Finance Manager")
OUTPUT = PROJECT / "documentation" / "Guia_del_Usuario_Gestor_Finanzas.pdf"
SHOTS = ROOT / "capturas"
RENDER = ROOT / "render"
PAGE_W, PAGE_H = landscape(A4)
MARGIN = 42
CONTENT_W = PAGE_W - 2 * MARGIN
INK = colors.HexColor("#173244")
TEAL = colors.HexColor("#126B61")
MUTED = colors.HexColor("#526572")
LIGHT = colors.HexColor("#F0F5F7")
LINE = colors.HexColor("#DAE3E8")
TOTAL_PAGES = 11


def register_fonts():
    """Embed Windows fonts so accents and currency symbols remain portable."""
    directory = Path(r"C:\Windows\Fonts")
    for name, filename in (("Guide", "segoeui.ttf"), ("GuideBold", "segoeuib.ttf")):
        pdfmetrics.registerFont(TTFont(name, str(directory / filename)))
    pdfmetrics.registerFontFamily("Guide", normal="Guide", bold="GuideBold", italic="Guide", boldItalic="GuideBold")


def paragraph(pdf, text, x, top, width, size=10.5, color=INK, bold=False, max_height=None):
    """Draw wrapped text and fail early instead of clipping content."""
    style = ParagraphStyle("body", fontName="GuideBold" if bold else "Guide", fontSize=size,
                           leading=size * 1.37, textColor=color, alignment=TA_LEFT, spaceAfter=0)
    item = Paragraph(text, style)
    _, height = item.wrap(width, PAGE_H)
    if max_height is not None and height > max_height:
        raise ValueError(f"El bloque de texto supera el espacio disponible: {text[:70]}")
    if top + height > PAGE_H - 38:
        raise ValueError(f"El texto invade el pie de página: {text[:70]}")
    item.drawOn(pdf, x, PAGE_H - top - height)
    return top + height


def label(pdf, text, x, top, size=9, color=MUTED):
    """Draw short labels without wrapping."""
    pdf.setFillColor(color)
    pdf.setFont("Guide", size)
    pdf.drawString(x, PAGE_H - top - size, text)


def base_page(pdf, number, title, subtitle):
    """Apply consistent navigation, margins, and page numbering."""
    pdf.setFillColor(colors.white)
    pdf.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    label(pdf, "GESTOR DE FINANZAS PERSONALES  /  GUÍA DEL USUARIO", MARGIN, 21, 8.2)
    pdf.setFillColor(TEAL)
    pdf.rect(MARGIN, PAGE_H - 41, 32, 3, stroke=0, fill=1)
    paragraph(pdf, title, MARGIN, 53, CONTENT_W, size=23, bold=True)
    paragraph(pdf, subtitle, MARGIN, 91, CONTENT_W, size=10.2, color=MUTED)
    pdf.setStrokeColor(LINE)
    pdf.line(MARGIN, 32, PAGE_W - MARGIN, 32)
    label(pdf, "Cesar Lanuza Urbina  ·  Guía actualizada el 23 de octubre de 2026", MARGIN, PAGE_H - 24, 8)
    pdf.setFillColor(MUTED)
    pdf.setFont("Guide", 8)
    pdf.drawRightString(PAGE_W - MARGIN, 16, f"{number} / {TOTAL_PAGES}")
    pdf.bookmarkPage(f"page{number}")
    pdf.addOutlineEntry(title, f"page{number}", level=0)


def image_box(pdf, filename, x, top, width, maximum_height, caption):
    """Place an authentic screenshot without distorting its aspect ratio."""
    path = SHOTS / filename
    with Image.open(path) as image:
        source_w, source_h = image.size
    scale = min((width - 12) / source_w, (maximum_height - 12) / source_h, 1.0)
    image_w, image_h = source_w * scale, source_h * scale
    frame_h = image_h + 12
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(LINE)
    pdf.roundRect(x, PAGE_H - top - frame_h, width, frame_h, 6, fill=1, stroke=1)
    pdf.drawImage(str(path), x + (width - image_w) / 2, PAGE_H - top - 6 - image_h,
                  width=image_w, height=image_h, preserveAspectRatio=True, mask="auto")
    paragraph(pdf, caption, x, top + frame_h + 6, width, size=8, color=MUTED)
    return top + frame_h + 25


def steps(pdf, items, x, top, width, size=10.2, gap=11):
    """Present short numbered actions in their actual order of execution."""
    for index, item in enumerate(items, 1):
        pdf.setFillColor(TEAL)
        pdf.circle(x + 8, PAGE_H - top - 8, 8, stroke=0, fill=1)
        pdf.setFillColor(colors.white)
        pdf.setFont("GuideBold", 8)
        pdf.drawCentredString(x + 8, PAGE_H - top - 11, str(index))
        bottom = paragraph(pdf, item, x + 26, top - 1, width - 26, size=size)
        top = max(top + 19, bottom) + gap
    return top


def note(pdf, title, text, x, top, width, height):
    """Highlight a rule that affects a user's next action."""
    pdf.setFillColor(LIGHT)
    pdf.roundRect(x, PAGE_H - top - height, width, height, 6, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.rect(x, PAGE_H - top - height, 3, height, fill=1, stroke=0)
    paragraph(pdf, title, x + 15, top + 10, width - 30, size=10, bold=True)
    paragraph(pdf, text, x + 15, top + 29, width - 30, size=9.4, max_height=height - 36)


def draw_cover(pdf):
    """Introduce the application and provide a compact navigation map."""
    pdf.setFillColor(LIGHT)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.rect(0, PAGE_H - 11, PAGE_W, 11, fill=1, stroke=0)
    label(pdf, "MANUAL DE USO  /  APLICACIÓN DE ESCRITORIO", MARGIN, 38, 9)
    paragraph(pdf, "Guía del usuario", MARGIN, 66, 710, size=32, bold=True)
    paragraph(pdf, "Gestor de Finanzas Personales", MARGIN, 113, 720, size=21)
    label(pdf, "Actualización: Editar y Eliminar  ·  23 de octubre de 2026", MARGIN, 154, 10)
    paragraph(pdf, "Propósito de la aplicación", MARGIN, 202, 260, size=15, bold=True)
    paragraph(pdf, "Registre sus ingresos y gastos en colones costarricenses, organícelos por categorías y consulte el balance de cada período. La aplicación guarda los cambios automáticamente en su equipo y permite exportar un resumen completo a CSV.",
              MARGIN, 233, 260, size=11)
    paragraph(pdf, "Esta guía explica las tareas habituales paso a paso. Las capturas originales usan datos ficticios. Las páginas 6 y 7 explican las nuevas acciones Editar y Eliminar, ubicadas debajo de la tabla.",
              MARGIN, 352, 260, size=10.3, color=MUTED)
    image_box(pdf, "01_principal.png", 325, 200, 474, 235,
              "Vista de demostración con categorías, movimientos y balance.")
    label(pdf, "CONTENIDO", MARGIN, 453, 8.8, TEAL)
    columns = [
        (MARGIN, [("02", "Inicio y pantalla principal"), ("03", "Categorías y colores"), ("04", "Registrar un ingreso"), ("05", "Registrar un gasto"), ("06", "Editar un movimiento")]),
        (MARGIN + 370, [("07", "Eliminar un movimiento"), ("08", "Filtrar por fechas"), ("09", "Exportar a CSV"), ("10", "Guardar y respaldar"), ("11", "Resolver errores")]),
    ]
    for x, items in columns:
        for i, (page, title) in enumerate(items):
            label(pdf, page, x, 475 + i * 15, 9, TEAL)
            label(pdf, title, x + 28, 475 + i * 15, 9)
    label(pdf, "Elaborado por Cesar Lanuza Urbina", MARGIN, PAGE_H - 25, 8)
    pdf.bookmarkPage("page1")
    pdf.addOutlineEntry("Guía del usuario", "page1", level=0)
    pdf.showPage()


def draw_dashboard(pdf):
    """Explain startup and the relationship between visible totals and rows."""
    base_page(pdf, 2, "Inicio y pantalla principal", "Abra la carpeta del proyecto y haga doble clic en start.bat.")
    image_box(pdf, "01_principal_detalle.png", MARGIN, 119, CONTENT_W, 333,
              "Figura 1. Captura original con datos ficticios. La versión actual añade Editar y Eliminar debajo de la tabla (páginas 6 y 7).")
    column = (CONTENT_W - 32) / 3
    for x, title, body in [
        (MARGIN, "1. Totales visibles", "Ingresos, gastos y balance corresponden a los movimientos que se muestran. Balance = ingresos - gastos."),
        (MARGIN + column + 16, "2. Acciones y categorías", "Use Nuevo ingreso, Nuevo gasto y Nueva categoría. El selector permite elegir una categoría para editarla."),
        (MARGIN + 2 * (column + 16), "3. Tabla y estado", "Seleccione una fila y pulse Editar o Eliminar debajo de la tabla. El mensaje inferior confirma las operaciones."),
    ]:
        paragraph(pdf, title, x, 474, column, size=10.5, bold=True)
        paragraph(pdf, body, x, 495, column, size=9.3)
    pdf.showPage()


def draw_categories(pdf):
    """Document creation and editing, including persistent category colors."""
    base_page(pdf, 3, "Crear y editar categorías", "Cree al menos una categoría antes de registrar ingresos o gastos.")
    gap = 26
    column = (CONTENT_W - gap) / 2
    image_box(pdf, "02_categoria_nueva.png", MARGIN, 123, column, 190,
              "Figura 2. Formulario de creación de categorías.")
    image_box(pdf, "03_categoria_editar.png", MARGIN + column + gap, 123, column, 190,
              "Figura 3. Edición de una categoría existente.")
    paragraph(pdf, "Crear una categoría", MARGIN, 332, column, size=13.5, bold=True)
    steps(pdf, ["Pulse <b>Nueva categoría</b>.", "Escriba un nombre, como <b>Entretenimiento</b>. Elija un color con <b>Elegir color</b> o ingrese un código como <b>#F5E5F8</b>.", "Pulse <b>Guardar</b>. La categoría quedará disponible en ambos tipos de movimiento."],
          MARGIN, 363, column, size=10)
    paragraph(pdf, "Editar nombre o color", MARGIN + column + gap, 332, column, size=13.5, bold=True)
    steps(pdf, ["Seleccione la categoría en <b>Editar categoría</b>, en la pantalla principal.", "Pulse <b>Editar nombre / color</b> y cambie los campos necesarios.", "Pulse <b>Guardar</b>. Sus movimientos mostrarán el nuevo nombre y color."],
          MARGIN + column + gap, 363, column, size=10)
    paragraph(pdf, "Reglas: nombre obligatorio, hasta 60 caracteres y sin duplicados aunque cambien las mayúsculas. El color se conserva al reiniciar. Cancelar cierra el formulario sin guardar.",
              MARGIN, 523, CONTENT_W, size=9.2, color=MUTED)
    pdf.showPage()


def draw_transaction(pdf, income=True):
    """Explain each separate transaction form using an authentic screenshot."""
    number = 4 if income else 5
    title = "Registrar un ingreso" if income else "Registrar un gasto"
    subtitle = "Registre el dinero que recibe, por ejemplo un salario o un pago por servicios." if income else "Registre sus compras y pagos utilizando siempre un monto positivo."
    base_page(pdf, number, title, subtitle)
    image_box(pdf, "04_ingreso.png" if income else "05_gasto.png", MARGIN, 127, 470, 312,
              "Figura 4. Ventana independiente para ingresos." if income else "Figura 5. Ventana independiente para gastos.")
    x = 537
    width = PAGE_W - MARGIN - x
    steps(pdf, [
        "Pulse <b>Nuevo ingreso</b>." if income else "Pulse <b>Nuevo gasto</b>.",
        "Complete <b>Título</b> con una descripción breve, de hasta 100 caracteres.",
        "Ingrese el <b>Monto en colones</b> sin separadores de miles. Ejemplo: <b>50000</b>." if income else "Ingrese el <b>Monto en colones</b> como un valor positivo. Ejemplo: <b>12500,50</b>.",
        "Seleccione una <b>Categoría</b> y revise la <b>Fecha</b>.",
        "Pulse <b>Guardar</b>. El registro aparecerá en la tabla y actualizará los totales. Si hay un filtro activo, su fecha debe pertenecer al intervalo para que sea visible.",
    ], x, 130, width, size=10, gap=10)
    note(pdf, "Formato del monto y de la fecha", "Se aceptan punto o coma decimal y hasta dos decimales; no se admiten cero ni montos negativos. La fecha debe ser real, usar dd/mm/aaaa y no ser futura.",
         MARGIN, 468, CONTENT_W, 75)
    pdf.showPage()


def draw_edit_transaction(pdf):
    """Explain selection, prefilled editing fields, saving, and cancellation."""
    base_page(pdf, 6, "Editar un movimiento", "Actualice un ingreso o gasto existente sin crear un registro adicional.")
    column = (CONTENT_W - 32) / 2
    x = MARGIN + column + 32
    paragraph(pdf, "Seleccionar y actualizar", MARGIN, 132, column, size=15, bold=True)
    steps(pdf, [
        "Seleccione con un clic la fila del movimiento en la tabla principal. Si no aparece, pulse <b>Quitar filtro</b> y búsquelo nuevamente.",
        "Pulse <b>Editar</b>, debajo de la tabla. Se abre el formulario <b>Editar movimiento</b> con los datos actuales.",
        "Modifique los campos necesarios y revise la información antes de continuar.",
        "Pulse <b>Guardar</b>. La aplicación guarda los cambios y actualiza la tabla, los colores y los totales visibles.",
    ], MARGIN, 170, column, size=10.5, gap=15)
    paragraph(pdf, "Campos que puede modificar", x, 132, column, size=15, bold=True)
    top = 169
    for title, body in [
        ("Título", "Descripción obligatoria de hasta 100 caracteres."),
        ("Monto en colones", "Valor positivo con hasta dos decimales, sin separadores de miles; por ejemplo, 12500,50."),
        ("Categoría y tipo", "Seleccione una categoría existente y el tipo Ingreso o Gasto. El tipo determina el signo del monto en la tabla."),
        ("Fecha", "Use dd/mm/aaaa, una fecha real y no futura."),
    ]:
        top = paragraph(pdf, title, x, top, column, size=10.5, bold=True) + 4
        top = paragraph(pdf, body, x, top, column, size=10.2) + 13
    note(pdf, "Cancelar o corregir", "<b>Cancelar</b> o cerrar el formulario descarta los cambios. Si un dato es inválido, el formulario permanece abierto para corregirlo. Si falla el guardado, el registro anterior se conserva.",
         MARGIN, 437, CONTENT_W, 73)
    paragraph(pdf, "El filtro activo se conserva. Si cambia la fecha fuera del intervalo, el movimiento deja de verse: pulse <b>Quitar filtro</b> para localizarlo. Después de actualizar la tabla, seleccione nuevamente una fila para otra acción.",
              MARGIN, 521, CONTENT_W, size=9.5, color=MUTED)
    pdf.showPage()


def draw_delete_transaction(pdf):
    """Explain the explicit confirmation required before a persisted deletion."""
    base_page(pdf, 7, "Eliminar un movimiento", "Revise el registro seleccionado antes de confirmar su eliminación.")
    column = (CONTENT_W - 32) / 2
    x = MARGIN + column + 32
    paragraph(pdf, "Seleccionar y confirmar", MARGIN, 132, column, size=15, bold=True)
    steps(pdf, [
        "Seleccione la fila del ingreso o gasto que desea eliminar en la tabla principal.",
        "Pulse <b>Eliminar</b>, debajo de la tabla. Se abre el popup <b>Confirmar eliminación</b>.",
        "Revise el título, la fecha, el tipo y el monto mostrados. Esto ayuda a distinguir registros con títulos repetidos.",
        "Pulse <b>Confirmar</b> para eliminar exclusivamente ese movimiento. La aplicación guarda el cambio en el archivo y actualiza la tabla y los totales.",
    ], MARGIN, 170, column, size=10.5, gap=16)
    paragraph(pdf, "Dos opciones en el popup", x, 132, column, size=15, bold=True)
    note(pdf, "Confirmar", "El registro se elimina del archivo de datos y ya no aparece al reiniciar. El resto de los movimientos y las categorías se conservan.",
         x, 171, column, 103)
    note(pdf, "Cancelar o cerrar", "Pulse <b>Cancelar</b> o cierre el popup con la X para conservar el registro. Ningún cambio se guarda por seleccionar la fila o abrir la confirmación.",
         x, 290, column, 103)
    note(pdf, "La eliminación confirmada no se puede deshacer", "La aplicación no tiene papelera ni botón Deshacer. Para recuperar un registro eliminado necesitará un respaldo válido; consulte <b>Guardar, respaldar y cerrar</b>, en la página 10.",
         MARGIN, 437, CONTENT_W, 73)
    paragraph(pdf, "El filtro activo se conserva y los totales se recalculan. Si falla el guardado, aparece un error y el movimiento permanece intacto. Los CSV ya exportados no cambian: vuelva a exportar para reflejar la edición o eliminación.",
              MARGIN, 521, CONTENT_W, size=9.5, color=MUTED)
    pdf.showPage()


def draw_filter(pdf):
    """Clarify inclusive date boundaries and the scope of filtered totals."""
    base_page(pdf, 8, "Filtrar movimientos por fechas", "Complete Desde y Hasta; luego pulse Filtrar. Ambos días se incluyen en el resultado.")
    image_box(pdf, "06_filtro_detalle.png", MARGIN, 122, CONTENT_W, 333,
              "Figura 6. Del 15/10/2026 al 22/10/2026: ingreso de 125.000,00, gastos de 24.500,00 y balance de 100.500,00 colones.")
    column = (CONTENT_W - 28) / 2
    paragraph(pdf, "Aplicar o quitar el filtro", MARGIN, 479, column, size=11, bold=True)
    paragraph(pdf, "Use dd/mm/aaaa y una fecha inicial anterior o igual a la final. Para volver a todos los registros, pulse <b>Quitar filtro</b>.",
              MARGIN, 503, column, size=10)
    paragraph(pdf, "Interpretar el resultado", MARGIN + column + 28, 479, column, size=11, bold=True)
    paragraph(pdf, "La tabla y los tres totales cambian juntos. Un intervalo sin movimientos muestra ceros. El filtro no elimina ni modifica datos.",
              MARGIN + column + 28, 503, column, size=10)
    pdf.showPage()


def draw_export(pdf):
    """Explain the native save dialog and the complete CSV export contract."""
    base_page(pdf, 9, "Exportar todos los movimientos a CSV", "El archivo puede abrirse en Excel u otra hoja de cálculo. Vuelva a exportar después de editar o eliminar.")
    image_box(pdf, "07_exportar.png", MARGIN, 127, CONTENT_W, 145,
              "Figura 7. Detalle del diálogo de Windows: nombre, tipo de archivo y botones de guardado.")
    column = (CONTENT_W - 28) / 2
    paragraph(pdf, "Guardar el archivo", MARGIN, 305, column, size=13, bold=True)
    steps(pdf, ["Pulse <b>Exportar todo a CSV</b> en la pantalla principal.",
                "Elija una carpeta escribible e indique un nombre terminado en <b>.csv</b>.",
                "Confirme con <b>Guardar</b> o <b>Save</b>, según el idioma de Windows. El mensaje inferior confirmará el resultado."],
          MARGIN, 337, column, size=10, gap=9)
    x = MARGIN + column + 28
    paragraph(pdf, "Revisar el contenido", x, 305, column, size=13, bold=True)
    paragraph(pdf, "El CSV contiene las columnas <b>Fecha, Título, Monto, Categoría y Tipo</b>. Al final aparecen total de ingresos, total de gastos y balance. Los montos usan punto decimal y no incluyen el símbolo monetario.",
              x, 337, column, size=10.5)
    paragraph(pdf, "Si su hoja de cálculo no separa las columnas automáticamente, importe el archivo como CSV con codificación UTF-8 y separador coma.",
              x, 414, column, size=10.2, color=MUTED)
    note(pdf, "El CSV siempre incluye todos los movimientos", "Aunque haya un filtro activo, la exportación incluye el historial completo. Los gastos llevan signo negativo; el total de gastos se presenta en valor absoluto. El balance es ingresos menos gastos.",
         MARGIN, 477, CONTENT_W, 66)
    pdf.showPage()


def draw_backup(pdf):
    """Provide user-level save, backup, restore, and first-install instructions."""
    base_page(pdf, 10, "Guardar, respaldar y cerrar", "Los cambios se guardan automáticamente después de cada operación confirmada.")
    column = (CONTENT_W - 32) / 2
    paragraph(pdf, "Durante el uso diario", MARGIN, 132, column, size=15, bold=True)
    paragraph(pdf, "Cada creación o edición se conserva al pulsar <b>Guardar</b>. Una eliminación se guarda al pulsar <b>Confirmar</b> en el popup. No necesita un guardado general. Para cerrar, use <b>Salir</b> o la X de la ventana.",
              MARGIN, 164, column, size=11)
    note(pdf, "Ubicación de sus datos", "Dentro de la carpeta del proyecto, el archivo <b>data/finanzas.json</b> conserva categorías, colores y movimientos. Se crea después del primer cambio guardado.",
         MARGIN, 263, column, 104)
    paragraph(pdf, "Volver a abrir", MARGIN, 390, column, size=13, bold=True)
    paragraph(pdf, "Ejecute <b>start.bat</b>. Los datos se restauran automáticamente. Solo se permite una instancia sobre el mismo archivo de datos.",
              MARGIN, 419, column, size=10.5)
    x = MARGIN + column + 32
    paragraph(pdf, "Crear un respaldo", x, 132, column, size=15, bold=True)
    steps(pdf, ["Cierre la aplicación.", "Copie <b>data/finanzas.json</b> a otra carpeta o dispositivo de confianza. Use un nombre que incluya la fecha del respaldo."],
          x, 166, column, size=10.5)
    paragraph(pdf, "Restaurar un respaldo", x, 274, column, size=13, bold=True)
    steps(pdf, ["Cierre la aplicación y conserve una copia del archivo actual.", "Reemplace <b>data/finanzas.json</b> por un respaldo válido y abra nuevamente el gestor."],
          x, 306, column, size=10.5)
    note(pdf, "Primera instalación en otro equipo", "Extraiga el ZIP completo. Necesita Windows y Python 3.11 o posterior con Tkinter. Ejecute <b>setup.bat</b> con Internet; después, <b>start.bat</b>. No copie la carpeta .venv de otro equipo.",
         MARGIN, 468, CONTENT_W, 75)
    pdf.showPage()


def draw_errors(pdf):
    """Explain recoverable validation messages and safe file-error handling."""
    base_page(pdf, 11, "Resolver errores frecuentes", "Lea el mensaje, pulse Aceptar y corrija el formulario. Los datos inválidos no se guardan.")
    image_box(pdf, "08_error.png", MARGIN, 127, 475, 196,
              "Figura 8. La aplicación rechaza un formulario incompleto con un mensaje en español.")
    paragraph(pdf, "Si un movimiento no aparece", 542, 133, 257, size=12, bold=True)
    paragraph(pdf, "Pulse <b>Quitar filtro</b> y revise su fecha. Si la operación mostró un error de guardado, corrija el problema y vuelva a intentarlo.",
              542, 163, 257, size=10.5)
    paragraph(pdf, "Si el programa no inicia", 542, 244, 257, size=12, bold=True)
    paragraph(pdf, "Ejecute <b>setup.bat</b> y luego <b>start.bat</b>. Si indica que el gestor ya está abierto, cierre la otra instancia.",
              542, 274, 257, size=10.5)
    rows = [
        ("Falta una categoría", "Cree una categoría y selecciónela antes de guardar el movimiento."),
        ("Nombre duplicado o vacío", "Use un nombre diferente y no deje campos obligatorios en blanco."),
        ("Monto no válido", "Use un valor mayor que cero y hasta dos decimales, sin separadores de miles."),
        ("Fecha o rango incorrectos", "Use dd/mm/aaaa, una fecha real y no futura para el movimiento; revise el orden del rango."),
        ("No se pudo guardar o exportar", "Revise permisos, espacio disponible y si el CSV está abierto en otra aplicación."),
        ("No se pudieron cargar los datos", "El archivo original se protege. Cierre el gestor, conserve una copia y restaure un respaldo válido."),
    ]
    top = 354
    for index, (problem, solution) in enumerate(rows):
        height = 30
        pdf.setFillColor(LIGHT if index % 2 == 0 else colors.white)
        pdf.rect(MARGIN, PAGE_H - top - height, CONTENT_W, height, fill=1, stroke=0)
        paragraph(pdf, problem, MARGIN + 10, top + 5, 183, size=9, bold=True)
        paragraph(pdf, solution, MARGIN + 207, top + 5, CONTENT_W - 217, size=9, max_height=27)
        top += height
    pdf.showPage()


def build_guide():
    """Generate the final PDF and render every page for visual quality assurance."""
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    RENDER.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    pdf.setTitle("Guía del usuario - Gestor de Finanzas Personales")
    pdf.setAuthor("Cesar Lanuza Urbina")
    pdf.setSubject("Manual de uso con capturas reales de la aplicación")
    pdf.setCreator("Gestor de Finanzas Personales - Documentación")
    draw_cover(pdf)
    draw_dashboard(pdf)
    draw_categories(pdf)
    draw_transaction(pdf, True)
    draw_transaction(pdf, False)
    draw_edit_transaction(pdf)
    draw_delete_transaction(pdf)
    draw_filter(pdf)
    draw_export(pdf)
    draw_backup(pdf)
    draw_errors(pdf)
    pdf.save()
    reader = PdfReader(OUTPUT)
    assert len(reader.pages) == TOTAL_PAGES
    full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    assert "Cesar Lanuza Urbina" in full_text
    assert "Exportar" in full_text and "respald" in full_text
    document = pymupdf.open(str(OUTPUT))
    for index, page in enumerate(document):
        pixmap = page.get_pixmap(matrix=pymupdf.Matrix(1.4, 1.4), alpha=False)
        pixmap.save(str(RENDER / f"pagina-{index + 1:02d}.png"))
    document.close()
    print(f"Guía generada: {OUTPUT}")
    print(f"Páginas verificadas y renderizadas: {TOTAL_PAGES}")


if __name__ == "__main__":
    build_guide()
