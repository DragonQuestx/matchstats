# === Stage 9: Группировка ===
# Project: MatchStats
def group_by_opponent(matches):
    groups = {}
    for match in matches:
        opponent = match.get('opponent')
        if opponent in groups:
            groups[opponent].append(match)
        else:
            groups[opponent] = [match]
    return groups


def count_by_opponent(matches):
    groups = group_by_opponent(matches)
    return {opponent: len(matches) for opponent, matches in groups.items()}


def group_and_count(matches):
    groups = group_by_opponent(matches)
    counts = {opponent: len(matches) for opponent, matches in groups.items()}
    result = []
    for opponent in sorted(groups.keys()):
        result.append({'opponent': opponent, 'count': counts[opponent], 'matches': groups[opponent]})
    return result
