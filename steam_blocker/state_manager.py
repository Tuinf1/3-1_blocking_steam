# state_manager.py
# Модуль отвечает за сохранение и загрузку состояния блокировки Steam.
# Он хранит информацию о том, заблокирован ли Steam сейчас
# и до какого времени действует блокировка.
#
# Связан с файлами:
# - config.py      — хранит путь к файлу состояния STATE_FILE
# - app_state.json — файл, куда сохраняется состояние блокировки
# - blocker.py     — вызывает load_state() и save_state()

import json

from config import STATE_FILE


# Начальное состояние приложения
DEFAULT_STATE = {
    "blocked": False,
    "blocked_until": None
}


# Создаём app_state.json, если его ещё нет
def create_state_file_if_not_exists() -> None:

    if not STATE_FILE.exists():
        save_state(DEFAULT_STATE)


# Загружаем состояние из app_state.json
def load_state() -> dict:

    create_state_file_if_not_exists()

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        # Если файл пустой или сломан — возвращаем начальное состояние
        save_state(DEFAULT_STATE)
        return DEFAULT_STATE


# Сохраняем состояние в app_state.json
def save_state(state: dict) -> None:

    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(
            state,
            file,
            ensure_ascii=False,
            indent=4
        )