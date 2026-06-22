# console_ui.py
# Модуль отвечает за консольное меню приложения.
# Через него пользователь выбирает действие: заблокировать Steam,
# проверить статус, разблокировать по коду или выйти из программы.
#
# Связан с файлами:
# - main.py    — запускает run_console_menu()
# - blocker.py — выполняет блокировку, проверку статуса и разблокировку

from steam_blocker.blocker import (
    block_steam,
    check_status,
    unblock_steam_by_code,
)


# Показываем главное меню
def show_menu() -> None:
    print()
    print("=== Steam Blocker ===")
    print("1. Заблокировать Steam")
    print("2. Проверить статус")
    print("3. Разблокировать по коду")
    print("4. Выход")
    print()


# Обрабатываем выбор пользователя
def handle_user_choice(choice: str) -> bool:

    # Блокировка Steam
    if choice == "1":
        block_steam()
        return True

    # Проверка текущего статуса
    if choice == "2":
        check_status()
        return True

    # Разблокировка по коду
    if choice == "3":
        user_code = input("Введите код разблокировки: ")
        unblock_steam_by_code(user_code)
        return True

    # Выход из программы
    if choice == "4":
        print("Выход из программы.")
        return False

    # Если пользователь ввёл неизвестную команду
    print("Неизвестная команда. Выберите пункт от 1 до 4.")
    return True


# Запускаем консольное меню в цикле
def run_console_menu() -> None:

    is_running = True

    # Пока пользователь не выбрал выход
    while is_running:
        show_menu()
        choice = input("Выберите действие: ").strip()
        is_running = handle_user_choice(choice)