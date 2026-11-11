# === Stage 4: Связи между сущностями ===
# Project: MatchStats
from datetime import datetime


class MatchEvent:
    def __init__(self, match, event_id, event_type, minute, description):
        self.match = match
        self.event_id = event_id
        self.event_type = event_type
        self.minute = minute
        self.description = description

    def __repr__(self):
        return (
            f"MatchEvent(id={self.event_id}, type={self.event_type}, "
            f"minute={self.minute}, description={self.description!r})"
        )


class Match:
    def __init__(self, date, home_team, away_team, home_score, away_score, venue):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.venue = venue
        self.events = []

    def add_event(self, event):
        if self.events and event.minute <= self.events[-1].minute:
            raise ValueError("события должны идти по возрастанию минут")
        self.events.append(event)

    def get_events(self):
        return list(self.events)


def check_event_integrity(match):
    if match is None:
        raise ValueError("матч не задан")

    if not isinstance(match, Match):
        raise TypeError("объект не является экземпляром Match")

    if match.home_score < 0 or match.away_score < 0:
        raise ValueError("счёт не может быть отрицательным")

    total_goals = match.home_score + match.away_score
    goal_events = [
        e for e in match.events
        if e.event_type in ("goal", "own_goal", "penalty")
    ]

    goals_by_minute = sorted(
        [e.minute for e in goal_events],
        key=lambda m: (m is None, m),
    )

    if len(goal_events) != total_goals:
        raise ValueError(
            f"несоответствие числа голов: в событиях "
            f"{len(goal_events)}, на табло {total_goals}"
        )

    for minute in goals_by_minute:
        if minute is not None and minute > 90:
            raise ValueError(f"гол за пределами времени игры: {minute}")

    for i in range(1, len(match.events)):
        previous = match.events[i - 1]
        current = match.events[i]
        if current.match is not match:
            raise ValueError("событие относится к другому матчу")
        if previous.minute is None or current.minute is None:
            continue
        if current.minute <= previous.minute:
            raise ValueError("события идут не по возрастанию минут")

    return match.events
