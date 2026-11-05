# === Stage 2: Проверка полей ===
# Project: MatchStats
from datetime import datetime


MATCH_DATE_FORMAT = "%Y-%m-%d"
VALID_PLACES = {"дом", "гост"}


def normalize_date(value):
    if isinstance(value, datetime):
        return value.strftime(MATCH_DATE_FORMAT)
    normalized = str(value).strip()
    if not normalized:
        return ""
    try:
        return datetime.strptime(normalized, MATCH_DATE_FORMAT).strftime(MATCH_DATE_FORMAT)
    except ValueError:
        raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")


def normalize_opponent(value):
    opponent = str(value).strip()
    if not opponent:
        raise ValueError("Соперник не может быть пустым")
    return opponent


def normalize_score(value):
    parts = str(value).strip().split()
    if len(parts) != 2:
        raise ValueError("Счёт должен состоять из двух чисел, например '2:1'")
    home_str, away_str = parts
    home, away = int(home_str), int(away_str)
    if home < 0 or away < 0:
        raise ValueError("Счёт не может быть отрицательным")
    return f"{home}:{away}"


def normalize_place(value):
    place = str(value).strip().lower()
    if place not in VALID_PLACES:
        raise ValueError("Место должно быть одним из: 'дом', 'гост'")
    return place


def validate_match(date, opponent, score, place):
    normalized_date = normalize_date(date)
    normalized_opponent = normalize_opponent(opponent)
    normalized_score = normalize_score(score)
    normalized_place = normalize_place(place)
    return {
        "date": normalized_date,
        "opponent": normalized_opponent,
        "score": normalized_score,
        "place": normalized_place,
    }
