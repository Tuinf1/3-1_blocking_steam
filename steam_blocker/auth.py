# auth.py

from config import UNLOCK_CODE


def normalize_code(code: str) -> str:
    """
    Очищает код от лишних пробелов.
    """

    return code.strip()


def verify_unlock_code(user_code: str) -> bool:
    """
    Проверяет код досрочной разблокировки Steam.
    """

    if not user_code:
        return False

    prepared_user_code = normalize_code(user_code)
    prepared_unlock_code = normalize_code(UNLOCK_CODE)

    return prepared_user_code == prepared_unlock_code