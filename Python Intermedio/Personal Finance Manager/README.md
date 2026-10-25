# Gestor de Finanzas Personales

Student: Cesar Lanuza Urbina  
Program: Manage personal income, expenses, categories, date filters, and CSV exports with a FreeSimpleGUI desktop interface.

Aplicación local de escritorio para registrar ingresos y gastos en colones costarricenses. Conserva automáticamente categorías, colores y movimientos en JSON. La interfaz y todos los mensajes propios de la aplicación están en español; los comentarios y la documentación de funciones del código están en inglés.

## Guía del usuario en PDF

Consulte [la guía del usuario](documentation/Guia_del_Usuario_Gestor_Finanzas.pdf): incluye introducción, instrucciones paso a paso, ocho capturas reales de pantallas con datos ficticios, edición y eliminación de movimientos, exportación, respaldos y solución de errores. La guía actualizada el 23 de octubre de 2026 tiene once páginas; las acciones Editar y Eliminar se explican en las páginas 6 y 7.

## Inicio en este equipo

El ambiente ya quedó instalado en `.venv` y las pruebas fueron ejecutadas.

1. Abra esta carpeta en el Explorador de Windows.
2. Haga doble clic en **start.bat**.
3. Cree una categoría con **Nueva categoría** y registre movimientos con **Nuevo ingreso** o **Nuevo gasto**.

También puede iniciar desde PowerShell:

```powershell
Set-Location -LiteralPath 'C:\Lyfter\Python Intermedio\Personal Finance Manager'
& '.\.venv\Scripts\python.exe' main.py
```

Use el intérprete `.venv\Scripts\python.exe` al abrir el proyecto en VS Code. Su configuración está incluida en `.vscode/settings.json`. Si ejecuta `main.py` con otro Python, deberá instalar allí las dependencias; los lanzadores utilizan siempre el entorno del proyecto.

## Instalar en otro equipo o reconstruir el ambiente

Requisitos: Windows, Python 3.11 o posterior con Tcl/Tk y acceso a Internet para la instalación inicial. Se verificó Windows con Python 3.14.6, Tk 8.6.15 y FreeSimpleGUI 5.3.0.post1.

Haga doble clic en **setup.bat**. El archivo crea un entorno aislado si hace falta, instala las versiones de `requirements-dev.txt` y comprueba las dependencias. No requiere permisos de administrador si la carpeta es escribible.

Instalación manual con Python 3.14:

```powershell
py -3.14 -m venv .venv
& '.\.venv\Scripts\python.exe' -m pip install -r requirements-dev.txt
& '.\.venv\Scripts\python.exe' -m pip check
```

`requirements.txt` contiene la dependencia de ejecución. `requirements-dev.txt` añade pytest y sus dependencias fijadas. Tkinter viene con la instalación de Python y no se instala con pip. No se necesita servidor, cuenta, servicio externo ni base de datos adicional.

## Uso

- **Nueva categoría:** nombre obligatorio, único sin distinguir mayúsculas y minúsculas, hasta 60 caracteres y color hexadecimal `#RRGGBB`. El botón **Elegir color** abre el selector nativo.
- **Editar nombre / color:** seleccione una categoría en la pantalla principal y abra su formulario. El identificador se conserva y todos sus movimientos muestran el nuevo nombre y color.
- **Nuevo ingreso / Nuevo gasto:** título obligatorio de hasta 100 caracteres, monto positivo con hasta dos decimales, categoría existente y fecha editable. Se aceptan `1500.25` y `1500,25`, sin separadores de miles. El importe máximo es `999999999999.99`.
- **Editar un movimiento:** seleccione su fila en la tabla y pulse **Editar**, debajo de la tabla. El formulario muestra los datos actuales y permite cambiar título, monto, categoría, tipo (Ingreso/Gasto) y fecha. Pulse **Guardar** para persistir los cambios o **Cancelar** para descartarlos. Cerrar el formulario también descarta los cambios. Se aplican las mismas validaciones que al registrar.
- **Eliminar un movimiento:** seleccione su fila y pulse **Eliminar**, debajo de la tabla. El popup muestra los datos del movimiento; **Confirmar** lo elimina del archivo JSON y **Cancelar** o cerrar el popup conserva el registro. La eliminación confirmada no se puede deshacer; use un respaldo si necesita recuperarlo.
- Al editar o eliminar se actualizan la tabla, los colores y los totales, conservando el filtro activo. Si la nueva fecha queda fuera del intervalo, el movimiento editado deja de aparecer hasta quitar o cambiar el filtro. Cada actualización de la tabla limpia la selección; seleccione nuevamente una fila antes de otra acción. La selección identifica el registro aunque existan títulos repetidos.
- La fecha sugerida es la actual del equipo. Se exige `dd/mm/aaaa`, una fecha real y no futura. La aplicación usa el calendario local configurado en Windows.
- **Filtrar:** complete Desde y Hasta. Los límites están incluidos y el inicio no puede ser posterior al fin. Se permiten límites futuros para consultar intervalos; no se permiten movimientos futuros. Los totales visibles corresponden al filtro.
- **Quitar filtro:** restaura todos los movimientos y sus totales.
- **Exportar todo a CSV:** exporta todos los movimientos aunque exista un filtro activo, con UTF-8 con BOM y columnas `Fecha,Título,Monto,Categoría,Tipo`. Los gastos llevan monto negativo; los totales de gastos son absolutos y el balance es ingresos menos gastos. Los importes se exportan con punto decimal y sin símbolo monetario.
- **Salir:** cierra la ventana. Cada cambio confirmado ya fue guardado, por lo que no se requiere un guardado adicional al salir.

Los títulos de movimientos pueden repetirse. Las categorías se comparten entre ingresos y gastos. No se incluye eliminación de categorías ni conversión de monedas, de acuerdo con el alcance del plan. La aplicación no contiene datos personales precargados.

La guía PDF también incluye las instrucciones de edición y eliminación de movimientos. Los CSV ya exportados son reportes independientes: para reflejar cambios, vuelva a exportarlos.

## Archivos de datos y recuperación

Los datos se generan en `data/finanzas.json` después del primer cambio exitoso. Los importes se conservan como texto decimal y las fechas internas como ISO `aaaa-mm-dd`. `data/finanzas.lock` impide abrir dos instancias sobre el mismo archivo de datos. Su existencia es normal; el bloqueo lo mantiene el proceso abierto y se libera al cerrarlo.

El guardado se realiza en un archivo temporal en la misma carpeta y luego mediante reemplazo. Si falla, la operación no se aplica en memoria y el archivo anterior permanece intacto. Si la carga falla por corrupción, esquema inválido o permisos, el programa avisa y termina sin reemplazar el archivo. No reinicializa datos silenciosamente.

Para respaldar, cierre el programa y copie `data/finanzas.json` a otra ubicación. Para restaurar, cierre el programa, conserve una copia del archivo actual y reemplace el JSON por un respaldo válido. Reinicie el gestor. Los respaldos son manuales; el guardado atómico no sustituye un respaldo histórico.

Para usar otro archivo local de datos durante una sesión:

```powershell
$env:GESTOR_FINANZAS_DATA = 'C:\ruta\finanzas.json'
& '.\.venv\Scripts\python.exe' main.py
Remove-Item Env:GESTOR_FINANZAS_DATA
```

## Nombres de funciones

Todas las funciones, métodos, propiedades y casos de prueba usan nombres en inglés, por ejemplo `create_category`, `record_transaction`, `edit_transaction`, `delete_transaction`, `calculate_totals`, `load`, `save` y `handle_event`. Los mensajes de la aplicación están en español. El esquema JSON existente sigue siendo compatible.

## Nombres de clases

Todas las clases usan nombres en inglés: `Category`, `Transaction`, `FinanceState`, `Totals`, `FinanceManager`, `FinanceRepository`, `CSVExporter`, `FinanceView`, `FinanceController`, `FinanceApplication`, `SingleInstanceLock`, `FinanceError`, `ValidationError`, `PersistenceError` y `ExportError`. Las importaciones y pruebas utilizan estos nombres. La auditoría del cambio está en `evidence/english_classes.json`.

## Pruebas y evidencia

La lógica no importa FreeSimpleGUI ni abre ventanas. Las pruebas siguen AAA y usan directorios temporales. Para ejecutarlas:

```powershell
& '.\.venv\Scripts\python.exe' -m pytest -v --junitxml=evidence\tests.xml
```

También puede usar **run_tests.bat**. Para repetir la integración gráfica con ventanas reales, datos temporales y exportación de muestra:

```powershell
& '.\.venv\Scripts\python.exe' verify_interface.py
```

Esta comprobación automatizada abre ventanas transparentes durante unos segundos. No modifica `data/finanzas.json`. El CSV de `evidence/sample_export.csv` usa exclusivamente datos ficticios y se vuelve a generar al ejecutarla.

Consulte `evidence/RESULTS.md` para las verificaciones realizadas y `TRACEABILITY.md` para la relación con los requerimientos RF-01 a RF-10 y RNF-01 a RNF-02 del plan.

## Estructura

```text
main.py                         Inicio y protección de instancia única
setup.bat                  Instalación o actualización del entorno
start.bat                     Inicio con el intérprete del proyecto
run_tests.bat             Ejecución de pytest
verify_interface.py            Integración automatizada con ventanas reales
finance_manager/
    models.py                  Categorías, movimientos, estado y totales
    validation.py             Texto, colores, importes y fechas
    logic.py                   Reglas de negocio y confirmación de cambios
    persistence.py             Carga validada y guardado JSON atómico
    export.py              CSV con totales
    controller.py              Acciones y datos listos para presentación
    interface.py                 Ventanas y eventos FreeSimpleGUI
    errors.py                  Errores propios en español
tests/                          Pruebas independientes de la interfaz
evidence/                      Resultados, XML de pytest y CSV ficticio
data/                           Datos locales generados durante el uso
```

El paquete de entrega omite `.venv`, datos reales y archivos temporales. Incluye código, dependencias, guía, pruebas y evidencia; ejecute `setup.bat` al extraerlo en otro equipo.

## Control de versiones y paquete de entrega

Git incluye el código, las pruebas, los lanzadores, la documentación y la evidencia. `.gitignore` excluye el entorno `.venv`, los datos personales de `data/`, las cachés, los archivos temporales y los ZIP generados.

Después de clonar el repositorio, abra esta carpeta y ejecute `setup.bat` para crear el entorno local. Para comprobar el proyecto y regenerar el paquete de entrega desde PowerShell:

```powershell
& '.\.venv\Scripts\python.exe' -m pytest -q
& '.\.venv\Scripts\python.exe' verify_interface.py
& '.\.venv\Scripts\python.exe' evidence\package.py
```

El último comando genera `Gestor_Finanzas_Personales.zip` con los archivos actuales. El ZIP no se versiona: vuelva a generarlo después de modificar el proyecto y antes de distribuirlo. Antes de confirmar cambios, revise `git status --short` y `git diff --check` desde esta carpeta.
