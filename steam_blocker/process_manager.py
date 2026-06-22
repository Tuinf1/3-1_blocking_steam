# process_manager.py
# Модуль отвечает за поиск и закрытие процессов Steam в Windows.
# Нужен, чтобы пользователь не мог запустить Steam во время активной блокировки.
#
# Связан с файлами:
# - config.py  — хранит список процессов STEAM_PROCESSES
# - blocker.py — вызывает close_steam_processes() при блокировке и проверке статуса
# - requirements.txt — должен содержать библиотеку psutil

import psutil
import subprocess

from config import STEAM_PROCESSES


# Проверяем, относится ли процесс к Steam
def is_steam_process(process_name: str) -> bool:
    return process_name.lower() in STEAM_PROCESSES


# Закрываем один найденный процесс
def close_process(process: psutil.Process) -> None:

    try:
        # Получаем имя процесса
        process_name = process.name()

        # Завершаем процесс
        process.terminate()

        print(f"Процесс закрыт: {process_name}")

    except psutil.NoSuchProcess:
        # Процесс уже закрылся сам
        pass

    except psutil.AccessDenied:
        # Нет прав на закрытие процесса
        print("Нет прав для закрытия процесса Steam. Запусти программу от администратора.")


# Закрываем все процессы Steam из списка STEAM_PROCESSES
def close_steam_processes(show_message: bool = True) -> None:
    """
    Закрывает процессы Steam через taskkill.

    show_message=False используется для фонового мониторинга,
    чтобы не спамить в консоль каждые 5 секунд.
    """
    steam_processes = [
        "steam.exe",
        "steamwebhelper.exe",
    ]

    for process_name in steam_processes:
        result = subprocess.run(
            ["taskkill", "/F", "/IM", process_name],
            capture_output=True,
            text=True
        )

        if show_message and result.returncode == 0:
            print(f"Процесс {process_name} закрыт.")