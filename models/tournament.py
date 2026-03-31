from datetime import datetime
from typing import List

class Tournament:
    def __init__(
        self,
        name: str,
        tournament_date: str,
        source: List[str],
        creation_date: datetime = None,
        update_date: datetime = None,
    ):
        self.name = name
        self.tournament_date = tournament_date
        self.source = source  # list of sources
        self.creation_date = creation_date or datetime.utcnow()
        self.update_date = update_date or datetime.utcnow()

    def add_source(self, new_source: str):
        """Add a source if it's not already included"""
        if new_source not in self.source:
            self.source.append(new_source)
            self.update_date = datetime.utcnow()

    def update_timestamp(self):
        self.update_date = datetime.utcnow()

    def __repr__(self):
        return (
            f"Tournament(name={self.name}, "
            f"tournament_date={self.tournament_date}, "
            f"source={self.source}, "
            f"created={self.creation_date}, "
            f"updated={self.update_date})"
        )
