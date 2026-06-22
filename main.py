# main.py
# Точка входа в приложение.
# Запускает консольное меню блокировщика Steam.

from ui.console_ui import run_console_menu


# Запускаем приложение
def main() -> None:
    run_console_menu()


if __name__ == "__main__":
    main()