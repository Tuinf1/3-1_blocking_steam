@echo off
chcp 65001 > nul

:: run_as_admin.bat
:: Запускает проект Steam Blocker.
::
:: Связан с файлами:
:: - main.py
:: - config.py
:: - steam_blocker/process_manager.py

cd /d "%~dp0.."

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
) else (
    python main.py
)

pause
