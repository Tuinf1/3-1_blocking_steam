# blocker.py

from datetime import datetime, timedelta
from config import BLOCK_MINUTES

import threading
import time
from steam_blocker.auth import verify_unlock_code
from steam_blocker.hosts_manager import block_steam_domains, unblock_steam_domains
from steam_blocker.process_manager import close_steam_processes
from steam_blocker.state_manager import load_state, save_state
from steam_blocker.timer import is_block_time_expired


def monitor_steam_processes():
    while load_state().get("blocked", False):
        close_steam_processes()
        time.sleep

def start_process_monitoring():
    """
    Запускает фоновую проверку процессов Steam.

    daemon=True означает, что поток автоматически завершится,
    когда пользователь закроет основную программу.
    """
    monitor_thread = threading.Thread(
        target=monitor_steam_processes,
        daemon=True
    )
    monitor_thread.start()


def block_steam() -> None:
    """
    Блокирует Steam:
    1. Закрывает процессы Steam.
    2. Добавляет домены Steam в hosts.
    3. Сохраняет состояние блокировки.
    """

    blocked_until = datetime.now() + timedelta(minutes=BLOCK_MINUTES)

    close_steam_processes()
    start_process_monitoring()
    block_steam_domains()

    save_state({
        "blocked": True,
        "blocked_until": blocked_until.strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"Steam заблокирован до {blocked_until.strftime('%Y-%m-%d %H:%M:%S')}")


def unblock_steam() -> None:
    """
    Полностью снимает блокировку Steam.
    """

    unblock_steam_domains()

    save_state({
        "blocked": False,
        "blocked_until": None
    })

    print("Steam разблокирован.")


def unblock_steam_by_code(user_code: str) -> None:
    """
    Разблокирует Steam только при правильном коде.
    """

    if verify_unlock_code(user_code):
        unblock_steam()
    else:
        print("Неверный код разблокировки.")


def check_status() -> None:
    """
    Проверяет текущее состояние блокировки.
    Если время блокировки прошло — автоматически разблокирует Steam.
    """

    state = load_state()

    if not state.get("blocked"):
        print("Steam сейчас не заблокирован.")
        return

    blocked_until = state.get("blocked_until")

    if blocked_until is None:
        print("Ошибка состояния: время окончания блокировки не найдено.")
        return

    if is_block_time_expired(blocked_until):
        print("Время блокировки истекло.")
        unblock_steam()
        return

    close_steam_processes()

    print(f"Steam заблокирован до {blocked_until}.")