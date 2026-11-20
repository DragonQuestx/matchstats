# === Stage 8: Теги ===
# Project: MatchStats
from datetime import date, datetime
from collections import defaultdict


class Tag:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Tag) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Tag({self.name!r})"


class Match:
    def __init__(self, match_id, date, home, away, home_score, away_score, location):
        self.match_id = match_id
        self.date = date
        self.home = home
        self.away = away
        self.home_score = home_score
        self.away_score = away_score
        self.location = location
        self.tags = set()

    def add_tag(self, tag):
        if not isinstance(tag, Tag):
            raise TypeError("Tag должен быть экземпляром класса Tag")
        self.tags.add(tag)

    def remove_tag(self, tag):
        if not isinstance(tag, Tag):
            raise TypeError("Tag должен быть экземпляром класса Tag")
        self.tags.discard(tag)

    def get_tags(self):
        return sorted(self.tags, key=lambda t: t.name)

    def get_tag(self, tag_name):
        return next((t for t in self.tags if t.name == tag_name), None)

    def has_tag(self, tag_name):
        return self.get_tag(tag_name) is not None

    def search_by_tag(self, tag_name):
        return [
            match for match in Match._all_matches
            if match.has_tag(tag_name)
        ]

    @staticmethod
    def _all_matches():
        return list(Match._match_store.values())

    @staticmethod
    def register(match):
        Match._match_store[match.match_id] = match

    @staticmethod
    def _match_store():
        return Match._match_store


Match._match_store = {}


def find_matches_by_tag(tag_name):
    return [
        match for match in Match._match_store.values()
        if match.has_tag(tag_name)
    ]
