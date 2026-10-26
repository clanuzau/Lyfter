@echo off
REM Student: Cesar Lanuza Urbina
REM Program: Run isolated pytest tests and save a machine-readable verification report.
setlocal
chcp 65001 >nul
pushd "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    call setup.bat
    if errorlevel 1 goto fail
)
".venv\Scripts\python.exe" -m pytest -v --junitxml=evidence\tests.xml
set "testResult=%errorlevel%"
if "%testResult%"=="0" (
    echo Todas las pruebas fueron exitosas.
) else (
    echo Una o mas pruebas fallaron. Revise el detalle anterior.
)
pause
popd
exit /b %testResult%
:fail
pause
popd
exit /b 1