@echo off
chcp 65001 > nul

:: unblock_emergency.bat
:: Аварийно снимает блокировку Steam без запуска Python-приложения.
:: Удаляет блок Steam из hosts и сбрасывает app_state.json.
::
:: Связан с файлами:
:: - C:\Windows\System32\drivers\etc\hosts
:: - app_state.json
:: - config.py
:: - steam_blocker/hosts_manager.py

net session >nul 2>&1

if %errorlevel% neq 0 (
    echo Запрашиваю права администратора...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

cd /d "%~dp0.."

powershell -Command ^
"$hostsPath = 'C:\Windows\System32\drivers\etc\hosts'; ^
$lines = Get-Content $hostsPath; ^
$newLines = @(); ^
$insideBlock = $false; ^
foreach ($line in $lines) { ^
    if ($line.Trim() -eq '# STEAM_BLOCKER START') { $insideBlock = $true; continue } ^
    if ($line.Trim() -eq '# STEAM_BLOCKER END') { $insideBlock = $false; continue } ^
    if (-not $insideBlock) { $newLines += $line } ^
}; ^
Set-Content -Path $hostsPath -Value $newLines -Encoding UTF8"

echo {
echo     "blocked": false,
echo     "blocked_until": null
echo } > app_state.json

echo Аварийная разблокировка выполнена.
pause