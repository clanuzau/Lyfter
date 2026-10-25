# Trazabilidad y decisiones de implementación

Implementación basada en el plan revisado de desarrollo del Gestor de Finanzas Personales, versión 1.0 del 22 de octubre de 2026. La solicitud del usuario autorizó la implementación; el estado de revisión indicado dentro del documento se trató como contexto del plan.

| Requerimiento | Implementación | Verificación |
| --- | --- | --- |
| RF-01 Tabla principal | FinanceApplication y FinanceController.get_view | Tabla vacía, dos tipos de movimiento y montos con signo en integración gráfica |
| RF-02 Categorías | create_category y formulario de categoría | tc001–tc003 e integración de formulario |
| RF-03 Gasto | record_transaction y ventana Gasto | tc005 y formulario gráfico |
| RF-04 Ingreso | record_transaction y ventana Ingreso | tc004 y formulario gráfico |
| RF-05 Sin categorías | Validación de servicio y bloqueo previo al formulario | tc006 e integración |
| RF-06 Persistencia | FinanceRepository y confirmación después de guardar | tc011, tc013 y tc016–tc021; recarga gráfica |
| RF-07 Filtro por fechas | validate_date_range y query_transactions | tc009–tc010, tc028–tc029 e integración |
| RF-08 Fecha editable no futura | Campo editable y validate_date | tc008 y rechazo de fecha futura en integración |
| RF-09 CSV con totales | CSVExporter y controlador.export | tc022–tc026 e integración con filtro activo |
| RF-10 Colores persistentes | edit_category, row_colors y contraste del texto | tc011, tc017, tc027 y consulta de colores reales en Treeview |
| Solicitud adicional: editar movimientos | edit_transaction, save_transaction y formulario precargado; identidad conservada | tests/test_transaction_changes.py e integración en verify_interface.py: campos, filtros, totales, recarga, cancelación y fallos de persistencia |
| Solicitud adicional: eliminar movimientos | delete_transaction, selección por ID y popup Confirmar/Cancelar | tests/test_transaction_changes.py e integración en verify_interface.py: confirmación, cancelación/cierre, títulos repetidos, CSV, recarga y fallos de persistencia |
| RNF-01 Modularidad y clases | Dominio, servicio, repositorio, exportador, controlador e interfaz separados | Importaciones de tests sin módulo GUI y archivos por responsabilidad |
| RNF-02 Mínimo ocho unitarias | Suite pytest con AAA y escenarios parametrizados | Consulte evidence/tests.xml y evidence/RESULTS.md para los resultados actualizados |

## Decisiones adoptadas

- D-01: JSON local con versión de esquema 1 y guardado atómico.
- D-02: moneda de presentación CRC, sin conversión de divisas.
- D-03: el CSV exporta todos los movimientos, independiente del filtro.
- D-04: edición de nombre y color; no eliminación de categorías.
- D-05: Windows y Python 3.14.6, verificados con FreeSimpleGUI 5.3.0.post1 y Tk 8.6.15.
- D-06: títulos repetidos permitidos; identidad única por movimiento.
- D-07: edición y eliminación de movimientos por identificador estable de la fila visible; botones debajo de la tabla, selección única y eliminación solo al confirmar explícitamente. La edición conserva el identificador y admite modificar todos los campos del movimiento. Ambas operaciones conservan el esquema JSON y el guardado atómico; los CSV anteriores se actualizan únicamente al volver a exportar.

Los gastos se almacenan como Decimal positivo; el tipo define su signo para la tabla y el CSV. Se rechazan montos con más de dos decimales en lugar de redondearlos silenciosamente. El guardado ocurre después de cada modificación confirmada; no hay cambios pendientes al cerrar. Se impide una segunda instancia sobre el mismo archivo para evitar sobrescrituras entre procesos.

## Disposición de la interfaz

La ventana principal presenta título y moneda, tres tarjetas de totales visibles, acciones de ingreso/gasto/categoría, selector para edición de categorías, rango de fechas, tabla y acciones de exportación y salida. Los formularios de categorías y de cada tipo de movimiento son ventanas modales independientes. Los errores conservan el formulario para corregir los valores. Se agrega texto claro al estado después de cada operación exitosa.

## Referencias técnicas consultadas

- FreeSimpleGUI en PyPI: https://pypi.org/project/FreeSimpleGUI/
- API de FreeSimpleGUI para Table.update y ColorChooserButton: https://freesimplegui.readthedocs.io/en/stable/call%20reference/

Las firmas de API y la actualización de colores se comprobaron también contra la biblioteca instalada.
