# === Stage 11: Поиск дубликатов ===
# Project: MatchStats
from datetime import date


def normalize_date(value):
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        parts = value.strip().split("-")
        if len(parts) == 3:
            return f"{parts[0]}-{parts[1]}-{parts[2]}"
        return value.strip().lower()
    if isinstance(value, (int, float)):
        return f"{int(value):04d}"
    return str(value).strip().lower()


def normalize_opponent(value):
    if value is None:
        return ""
    return " ".join(str(value).split()).lower().strip()


def normalize_score(value):
    if value is None:
        return None
    parts = str(value).split()
    if len(parts) == 2:
        try:
            return (int(parts[0]), int(parts[1]))
        except ValueError:
            return str(value).strip().lower()
    return str(value).strip().lower()


def normalize_venue(value):
    if value is None:
        return ""
    return " ".join(str(value).split()).lower().strip()


def normalize_match(match):
    return (
        normalize_date(getattr(match, "date", None)),
        normalize_opponent(getattr(match, "opponent", None)),
        normalize_score(getattr(match, "score", None)),
        normalize_venue(getattr(match, "venue", None)),
    )


def find_duplicate_matches(matches):
    seen = {}
    duplicates = []
    for match in matches:
        key = normalize_match(match)
        if key in seen:
            duplicates.append((seen[key], match))
        else:
            seen[key] = match
    return duplicates
