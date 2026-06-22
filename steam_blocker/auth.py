from config import UNLOCK_CODE

# auth.py
# Модуль отвечает за проверку кода досрочной разблокировки Steam.
# Код разблокировки хранится в .env, загружается в config.py
# и используется здесь для сравнения с кодом, который ввёл пользователь.
#
# Связан с файлами:
# - .env          — хранит UNLOCK_CODE
# - config.py    — загружает UNLOCK_CODE из .env
# - blocker.py   — вызывает verify_unlock_code() перед разблокировкой
# - console_ui.py — получает код от пользователя через консольное меню

# Убираем пробелы в начале и конце строки
def normalize_code(code: str) -> str:
    return code.strip()


# Проверяем код разблокировки
def verify_unlock_code(user_code: str) -> bool:

    # Если код не введён
    if not user_code:
        return False

    # Подготавливаем код пользователя
    prepared_user_code = normalize_code(user_code)

    # Подготавливаем код из .env
    prepared_unlock_code = normalize_code(UNLOCK_CODE)

    # Сравниваем коды
    return prepared_user_code == prepared_unlock_code