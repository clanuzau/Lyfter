@echo off
REM Student: Cesar Lanuza Urbina
REM Program: Configure an isolated Python environment and install pinned project dependencies.
setlocal
chcp 65001 >nul
pushd "%~dp0"
if exist ".venv\Scripts\python.exe" goto install
REM Prefer Python 3.14, then fall back to an available Python 3 installation.
py -3.14 -c "import sys; sys.exit(not (sys.version_info >= (3, 11)))" >nul 2>nul
if not errorlevel 1 (
    py -3.14 -m venv .venv
    goto created
)
py -3 -c "import sys; sys.exit(not (sys.version_info >= (3, 11)))" >nul 2>nul
if not errorlevel 1 (
    py -3 -m venv .venv
    goto created
)
python -c "import sys; sys.exit(not (sys.version_info >= (3, 11)))" >nul 2>nul
if errorlevel 1 (
    echo No se encontro Python 3.11 o posterior. Instale Python con Tkinter y vuelva a ejecutar este archivo.
    goto fail
)
python -m venv .venv
:created
if errorlevel 1 goto fail
:install
".venv\Scripts\python.exe" -m pip install -r requirements-dev.txt
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -m pip check
if errorlevel 1 goto fail
".venv\Scripts\python.exe" -c "import tkinter, FreeSimpleGUI, pytest"
if errorlevel 1 goto fail
echo Ambiente configurado correctamente. Ejecute start.bat para abrir el gestor.
popd
exit /b 0
:fail
echo No se pudo configurar el ambiente. Revise Python, la conexion a Internet y los permisos.
popd
exit /b 1