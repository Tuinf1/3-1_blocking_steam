@echo off
chcp 65001 > nul

:: run_as_admin.bat
:: Запускает проект Steam Blocker от имени администратора.
:: Нужен, потому что для изменения Windows hosts требуются права администратора.
::
:: Связан с файлами:
:: - main.py
:: - config.py
:: - steam_blocker/hosts_manager.py

net session >nul 2>&1

if %errorlevel% neq 0 (
    echo Запрашиваю права администратора...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

cd /d "%~dp0.."

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
) else (
    python main.py
)

pause