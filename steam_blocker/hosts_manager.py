# hosts_manager.py
# Модуль отвечает за добавление и удаление блокировки Steam в файле Windows hosts.
# Он записывает домены Steam как 127.0.0.1, из-за чего они перестают открываться.
#
# Связан с файлами:
# - config.py  — хранит HOSTS_PATH, STEAM_DOMAINS и HOSTS_MARKER
# - blocker.py — вызывает block_steam_domains() и unblock_steam_domains()
# - main.py    — приложение нужно запускать от администратора, иначе hosts не изменится

from config import HOSTS_MARKER, HOSTS_PATH, STEAM_DOMAINS


# Формируем строки для блокировки доменов Steam
def build_block_lines() -> list[str]:

    block_lines = []

    # Добавляем начало блока, чтобы потом легко найти наши строки
    block_lines.append(f"{HOSTS_MARKER} START\n")

    # Для каждого домена создаём строку блокировки
    for domain in STEAM_DOMAINS:
        block_lines.append(f"127.0.0.1 {domain}\n")

    # Добавляем конец блока
    block_lines.append(f"{HOSTS_MARKER} END\n")

    return block_lines


# Читаем содержимое hosts
def read_hosts_file() -> list[str]:

    try:
        with open(HOSTS_PATH, "r", encoding="utf-8") as file:
            return file.readlines()

    except PermissionError:
        print("Нет прав для чтения hosts. Запусти программу от администратора.")
        return []


# Записываем новое содержимое в hosts
def write_hosts_file(lines: list[str]) -> None:

    try:
        with open(HOSTS_PATH, "w", encoding="utf-8") as file:
            file.writelines(lines)

    except PermissionError:
        print("Нет прав для записи в hosts. Запусти программу от администратора.")


# Проверяем, есть ли уже блокировка Steam в hosts
def is_steam_block_exists(lines: list[str]) -> bool:

    # Ищем наш маркер в файле hosts
    for line in lines:
        if HOSTS_MARKER in line:
            return True

    return False


# Удаляем старый блок Steam из hosts
def remove_steam_block(lines: list[str]) -> list[str]:

    new_lines = []
    inside_steam_block = False

    # Проходим по всем строкам hosts
    for line in lines:

        # Нашли начало блока Steam
        if line.strip() == f"{HOSTS_MARKER} START":
            inside_steam_block = True
            continue

        # Нашли конец блока Steam
        if line.strip() == f"{HOSTS_MARKER} END":
            inside_steam_block = False
            continue

        # Оставляем только строки вне блока Steam
        if not inside_steam_block:
            new_lines.append(line)

    return new_lines


# Добавляем блокировку доменов Steam в hosts
def block_steam_domains() -> None:

    # Читаем текущий hosts
    lines = read_hosts_file()

    # Если файл не прочитался
    if not lines:
        return

    # Сначала удаляем старый блок, чтобы не было дублей
    lines_without_old_block = remove_steam_block(lines)

    # Добавляем пустую строку и новый блок Steam
    new_lines = lines_without_old_block
    new_lines.append("\n")
    new_lines.extend(build_block_lines())

    # Записываем обновлённый hosts
    write_hosts_file(new_lines)

    print("Домены Steam добавлены в hosts.")


# Удаляем блокировку доменов Steam из hosts
def unblock_steam_domains() -> None:

    # Читаем текущий hosts
    lines = read_hosts_file()

    # Если файл не прочитался
    if not lines:
        return

    # Удаляем блок Steam
    new_lines = remove_steam_block(lines)

    # Записываем очищенный hosts
    write_hosts_file(new_lines)

    print("Домены Steam удалены из hosts.")