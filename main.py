# main.py
# Точка входа в приложение.
# Запускает консольное меню блокировщика Steam.

from ui.console_ui import run_console_menu
from steam_blocker.state_manager import load_state
from steam_blocker.process_manager import close_steam_processes
from steam_blocker.blocker import start_process_monitoring

# Запускаем приложение
def main() -> None:
    
    state = load_state()

    if state.get("blocked", False):
        close_steam_processes()
        start_process_monitoring()
    run_console_menu()
if __name__ == "__main__":
    main()