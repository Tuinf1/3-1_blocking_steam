# Steam Blocker

Консольное Python-приложение для временной блокировки Steam без изменения системного файла Windows.

Проект закрывает процессы Steam, сохраняет состояние блокировки в `app_state.json` и позволяет досрочно снять блокировку только по коду.

## Как работает

1. Пользователь выбирает пункт `Заблокировать Steam`.
2. Программа закрывает процессы Steam.
3. Программа сохраняет время окончания блокировки.
4. Пока блокировка активна, фоновый поток каждые несколько секунд снова закрывает Steam, если он был открыт повторно.
5. Разблокировка возможна после окончания таймера или по коду.

## Структура проекта

```text
06_blocking_steam/
├── main.py
├── config.py
├── app_state.json
├── requirements.txt
├── scripts/
│   ├── run_as_admin.bat
│   └── unblock_emergency.bat
├── steam_blocker/
│   ├── __init__.py
│   ├── auth.py
│   ├── blocker.py
│   ├── logger.py
│   ├── process_manager.py
│   ├── state_manager.py
│   └── timer.py
└── ui/
    ├── __init__.py
    └── console_ui.py
```

## Главное

Вся блокировка построена только на закрытии процессов Steam.

## Запуск

```bash
python main.py
```

Или через bat-файл:

```text
scripts/run_as_admin.bat
```

## Настройки

Настройки находятся в `config.py` и `.env`.

Основные параметры:

```text
UNLOCK_CODE=123456
BLOCK_MINUTES=120
```

## Аварийная разблокировка

Если нужно сбросить состояние блокировки вручную, запусти:

```text
scripts/unblock_emergency.bat
```

Он меняет только `app_state.json` и не трогает системные файлы Windows.
