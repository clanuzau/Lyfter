@echo off
REM Student: Cesar Lanuza Urbina
REM Program: Launch the finance desktop application using its local virtual environment.
setlocal
chcp 65001 >nul
pushd "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    call setup.bat
    if errorlevel 1 goto fail
)
".venv\Scripts\python.exe" main.py
set "appResult=%errorlevel%"
if not "%appResult%"=="0" (
    echo La aplicacion no pudo terminar correctamente. Revise el mensaje anterior.
    pause
)
popd
exit /b %appResult%
:fail
pause
popd
exit /b 1