@echo off
chcp 65001 >nul

:: unblock_emergency.bat
:: Аварийно сбрасывает состояние блокировки.
::
:: Скрипт нужен, если программа сломалась или код разблокировки забыт.

cd /d "%~dp0.."

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"$statePath = Join-Path (Get-Location) 'app_state.json'; ^
$state = '{"blocked": false, "blocked_until": null}'; ^
Set-Content -Path $statePath -Value $state -Encoding UTF8; ^
Write-Output 'Состояние блокировки сброшено.'"

pause
