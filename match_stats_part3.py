# === Stage 3: Хранилище в памяти ===
# Project: MatchStats
memory_store.py

import uuid


class MemoryMatchStore:
    def __init__(self):
        self._matches = {}
        self._counter = 0

    def add_match(self, date, opponent, score, place):
        match_id = str(uuid.uuid4())
        self._matches[match_id] = {
            'id': match_id,
            'date': date,
            'opponent': opponent,
            'score': score,
            'place': place,
        }
        self._counter += 1
        return match_id

    def get_match(self, match_id):
        return self._matches.get(match_id)

    def list_matches(self):
        ordered = []
        for match_id in sorted(self._matches.keys(), key=lambda m: self._matches[m]['id']):
            ordered.append(self._matches[match_id])
        return ordered


if __name__ == '__main__':
    store = MemoryMatchStore()
    m1 = store.add_match('2024-05-01', 'Team B', 2, 'home')
    m2 = store.add_match('2024-05-03', 'Team C', 1, 'away')
    print('Match 1:', store.get_match(m1))
    print('Match 2:', store.get_match(m2))
    print('All matches:')
    for match in store.list_matches():
        print(match)
    print('Total matches:', len(store.list_matches()))
