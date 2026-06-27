# logger.py
# Модуль отвечает за настройку логирования приложения.
# Он создаёт папку logs, файл logs/app.log и настраивает запись событий:
# блокировка Steam, разблокировка, ошибки доступа, неверный код и другие действия.
#
# Связан с файлами:
# - logs/app.log          — файл, куда сохраняются логи
# - blocker.py           — может записывать события блокировки и разблокировки
# - process_manager.py   — может записывать закрытие процессов Steam
# - auth.py              — может записывать неверные попытки ввода кода
# - state_manager.py     — может записывать ошибки чтения app_state.json

import logging
from pathlib import Path


# Корневая папка проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# Папка для логов
LOG_DIR = BASE_DIR / "logs"


# Файл логов
LOG_FILE = LOG_DIR / "app.log"


# Создаём папку logs, если её нет
LOG_DIR.mkdir(exist_ok=True)


# Настраиваем общий логгер приложения
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


# Создаём логгер, который можно импортировать в других файлах
logger = logging.getLogger("steam_blocker")