# === Stage 1: Каркас модуля ===
# Project: MatchStats
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Score:
    home: int
    away: int


@dataclass
class Match:
    date: date
    opponent: str
    score: Score
    place: str
    goals: List[dict] = field(default_factory=list)


def make_demo_matches() -> List[Match]:
    d = date(2024, 5, 15)
    e = date(2024, 5, 22)
    f = date(2024, 5, 29)
    return [
        Match(d, "Авангард", Score(2, 1), "Дома",
              goals=[{"minute": 12, "team": "home"},
                     {"minute": 45, "team": "away"},
                     {"minute": 88, "team": "home"}]),
        Match(e, "Торпедо", Score(0, 0), "На выезде"),
        Match(f, "Спартак", Score(3, 2), "Дома",
              goals=[{"minute": 5, "team": "away"},
                     {"minute": 30, "team": "home"},
                     {"minute": 67, "team": "home"},
                     {"minute": 71, "team": "away"},
                     {"minute": 90, "team": "home"}]),
    ]


def main() -> None:
    matches = make_demo_matches()
    for m in matches:
        print(f"{m.date} {m.place}: {m.opponent} {m.score.home}-{m.score.away}")
        print(f"  Голы: {len(m.goals)}")
    print(f"Всего матчей: {len(matches)}")


if __name__ == "__main__":
    main()
