# config.py

from pathlib import Path
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# Корневая папка проекта
BASE_DIR = Path(__file__).resolve().parent

# Файл состояния блокировки
STATE_FILE = BASE_DIR / "state.json"

# Путь к hosts Windows
HOSTS_PATH = Path(
    r"C:\Windows\System32\drivers\etc\hosts"
)

# Код разблокировки
UNLOCK_CODE = os.getenv(
    "UNLOCK_CODE",
    "123456"
)

# Длительность блокировки в минутах
BLOCK_MINUTES = int(
    os.getenv(
        "BLOCK_MINUTES",
        "120"
    )
)

# Процессы Steam, которые нужно закрывать
STEAM_PROCESSES = [
    "steam.exe",
    "steamwebhelper.exe",
]

# Домены Steam для блокировки через hosts
STEAM_DOMAINS = [
    "store.steampowered.com",
    "steamcommunity.com",
    "steamcdn-a.akamaihd.net",
    "steamstatic.com",
    "api.steampowered.com",
]

# Строка-маркер, чтобы легко удалять блокировки
HOSTS_MARKER = "# STEAM_BLOCKER"

# Проверка настроек
if BLOCK_MINUTES <= 0:
    raise ValueError(
        "BLOCK_MINUTES должен быть больше 0"
    )