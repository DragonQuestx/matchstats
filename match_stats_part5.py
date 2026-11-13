# === Stage 5: Сортировка записей ===
# Project: MatchStats
from datetime import datetime


def parse_date(raw):
    """Преобразует строку даты в объект datetime для сортировки."""
    return datetime.fromisoformat(raw)


def sort_key(match):
    """Ключ сортировки для записи матча.

    Сортирует по дате и по дате создания.
    Дата может храниться как строка или как объект datetime.
    """
    date_value = match["date"]
    if isinstance(date_value, str):
        date_value = parse_date(date_value)
    return (date_value, match.get("created_at", datetime.min))


def sort_matches(matches, reverse=False):
    """Сортирует список записей «матч» по дате и дате создания.

    Args:
        matches: список словарей с полями «date» и «created_at».
        reverse: если True, сортировка по убыванию.

    Returns:
        новый отсортированный список.
    """
    return sorted(matches, key=sort_key, reverse=reverse)


def sort_by_created(matches, reverse=False):
    """Сортирует записи «матч» только по дате создания.

    Args:
        matches: список словарей с полем «created_at».
        reverse: если True, сортировка по убыванию.

    Returns:
        новый отсортированный список.
    """
    return sorted(matches, key=lambda m: m.get("created_at", datetime.min),
                  reverse=reverse)


def sort_by_date_string(matches, reverse=False):
    """Сортирует записи «матч» по строковому полю «date».

    Используется, когда дата уже хранится в нормализованном формате
    и не требует дополнительной обработки.

    Args:
        matches: список словарей с полем «date».
        reverse: если True, сортировка по убыванию.

    Returns:
        новый отсортированный список.
    """
    return sorted(matches, key=lambda m: m.get("date", ""), reverse=reverse)


if __name__ == "__main__":
    demo = [
        {"date": "2024-05-01", "created_at": "2024-05-02T10:00:00"},
        {"date": "2024-04-15", "created_at": "2024-04-16T09:00:00"},
        {"date": "2024-06-10", "created_at": "2024-05-01T08:00:00"},
    ]
    print(sort_matches(demo))
    print(sort_matches(demo, reverse=True))
    print(sort_by_created(demo, reverse=True))
