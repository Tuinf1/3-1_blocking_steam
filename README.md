Что за что отвечает
main.py

Точка входа. Запускает приложение.

config.py

Настройки: путь к Steam, список доменов Steam, длительность блокировки.

blocker.py

Главная логика блокировки и разблокировки.

timer.py

Следит, сколько времени осталось до конца блокировки.

auth.py

Проверяет код разблокировки.

process_manager.py

Закрывает процессы Steam:

steam.exe
steamwebhelper.exe
hosts_manager.py

Добавляет или удаляет блокировку доменов Steam в файле Windows hosts.

state_manager.py

Хранит состояние:

{
  "blocked": true,
  "blocked_until": "2026-06-20 20:00:00"
}
console_ui.py

Консольное меню:

1. Заблокировать Steam
2. Проверить статус
3. Разблокировать по коду
4. Выход
requirements.txt
psutil
python-dotenv
Пример .env.example
UNLOCK_CODE=123456
BLOCK_MINUTES=120
Логика работы
Пользователь запускает программу от администратора
        ↓
Выбирает "Заблокировать Steam"
        ↓
Программа закрывает steam.exe
        ↓
Добавляет домены Steam в hosts
        ↓
Сохраняет время окончания блокировки
        ↓
Пока время не прошло — Steam закрывается снова
        ↓
Для досрочного снятия блокировки нужен код
Домены для блокировки
STEAM_DOMAINS = [
    "store.steampowered.com",
    "steamcommunity.com",
    "steamcdn-a.akamaihd.net",
    "steamstatic.com",
    "api.steampowered.com",
]