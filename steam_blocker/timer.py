# timer.py

from datetime import datetime


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_blocked_until(blocked_until: str) -> datetime:
    """
    Преобразует строку из app_state.json в datetime.
    """

    return datetime.strptime(blocked_until, DATETIME_FORMAT)


def is_block_time_expired(blocked_until: str) -> bool:
    """
    Проверяет, истекло ли время блокировки.
    """

    blocked_until_datetime = parse_blocked_until(blocked_until)

    return datetime.now() >= blocked_until_datetime


def get_remaining_seconds(blocked_until: str) -> int:
    """
    Возвращает, сколько секунд осталось до конца блокировки.
    """

    blocked_until_datetime = parse_blocked_until(blocked_until)
    remaining_time = blocked_until_datetime - datetime.now()

    remaining_seconds = int(remaining_time.total_seconds())

    if remaining_seconds < 0:
        return 0

    return remaining_seconds


def get_remaining_time_text(blocked_until: str) -> str:
    """
    Возвращает оставшееся время в понятном виде.
    Например: 1 ч. 25 мин. 10 сек.
    """

    remaining_seconds = get_remaining_seconds(blocked_until)

    hours = remaining_seconds // 3600
    minutes = (remaining_seconds % 3600) // 60
    seconds = remaining_seconds % 60

    return f"{hours} ч. {minutes} мин. {seconds} сек."