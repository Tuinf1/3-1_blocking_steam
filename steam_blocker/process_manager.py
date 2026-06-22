# process_manager.py
# Модуль отвечает за поиск и закрытие процессов Steam в Windows.
# Нужен, чтобы пользователь не мог запустить Steam во время активной блокировки.
#
# Связан с файлами:
# - config.py  — хранит список процессов STEAM_PROCESSES
# - blocker.py — вызывает close_steam_processes() при блокировке и проверке статуса
# - requirements.txt — должен содержать библиотеку psutil

import psutil

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
def close_steam_processes() -> None:

    # Перебираем все запущенные процессы Windows
    for process in psutil.process_iter(["name"]):

        try:
            # Получаем имя процесса
            process_name = process.info["name"]

            # Если имя процесса пустое — пропускаем
            if not process_name:
                continue

            # Проверяем, является ли процесс процессом Steam
            if is_steam_process(process_name):
                close_process(process)

        except psutil.NoSuchProcess:
            # Процесс исчез во время проверки
            pass

        except psutil.AccessDenied:
            # Нет доступа к процессу
            pass