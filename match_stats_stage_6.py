# === Stage 6: Текстовый поиск ===
# Project: MatchStats
def search_matches(matches, query):
    query = query.strip().lower()
    if not query:
        return []
    results = []
    for match in matches:
        fields = [match.get('date', ''), match.get('opponent', ''), match.get('score', ''), match.get('venue', '')]
        text = ' '.join(fields).lower()
        if query in text:
            results.append(_highlight_match(match, query))
    return results


def _highlight_match(match, query):
    def highlight(text, query):
        text = text.replace(query, '<mark>' + query + '</mark>')
        return text

    date = highlight(match.get('date', ''), query)
    opponent = highlight(match.get('opponent', ''), query)
    score = highlight(match.get('score', ''), query)
    venue = highlight(match.get('venue', ''), query)
    return {
        'date': date,
        'opponent': opponent,
        'score': score,
        'venue': venue,
    }


if __name__ == '__main__':
    matches = [
        {'date': '2024-05-10', 'opponent': 'Arsenal', 'score': '2-1', 'venue': 'home'},
        {'date': '2024-05-15', 'opponent': 'Chelsea', 'score': '0-3', 'venue': 'away'},
        {'date': '2024-06-01', 'opponent': 'Liverpool', 'score': '4-0', 'venue': 'home'},
    ]
    for found in search_matches(matches, 'arsenal'):
        print(found['date'], found['opponent'], found['score'], found['venue'])
    for found in search_matches(matches, 'home'):
        print(found['date'], found['opponent'], found['score'], found['venue'])
