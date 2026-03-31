from scrapers.base import BaseScraper
from models.tournament import Tournament

class TestScrapper(BaseScraper):

    def scrape(self):
        # Dummy implementation
        return [
            Tournament("Tournament A1", "2026-04-01", "Riga"),
            Tournament("Tournament A2", "2026-04-05", "Tallinn"),
        ]
