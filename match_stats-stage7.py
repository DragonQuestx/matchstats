# === Stage 7: Поиск по нескольким словам ===
# Project: MatchStats
def search_matches(matches, query):
    words = []
    exclusions = []
    for token in query.replace("-", " ").split():
        if token.startswith("-"):
            exclusions.append(token[1:].lower())
        else:
            words.append(token.lower())

    results = []
    for match in matches:
        haystack = " ".join(
            [
                match.get("date", "").lower(),
                match.get("opponent", "").lower(),
                match.get("score", "").lower(),
                match.get("venue", "").lower(),
            ]
        )
        if any(word in haystack for word in words):
            if not any(word in haystack for word in exclusions):
                results.append(match)

    return results


if __name__ == "__main__":
    sample = [
        {"date": "2024-03-01", "opponent": "Arsenal", "score": "2-1", "venue": "Home"},
        {"date": "2024-03-05", "opponent": "Chelsea", "score": "0-3", "venue": "Away"},
        {"date": "2024-03-10", "opponent": "Man City", "score": "4-2", "venue": "Home"},
    ]

    print(search_matches(sample, "man city"))
    print(search_matches(sample, "away -chelsea"))
    print(search_matches(sample, "arsenal chelsea -chelsea"))
