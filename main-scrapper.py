from scrapers.saha_federacija import SahaFederacijaScraper
from scrapers.sahaskola import SahaSkolaScraper
from database.tournament_repository import TournamentRepository

class MainScraper:
    def __init__(self):
        self.sources = self._load_sources()

    def _load_sources(self):
        """
        Register all scraper sources here.
        """
        return [
            SahaFederacijaScraper(),
            SahaSkolaScraper()
        ]

    def scrap_data(self):
        """
        Runs all scrapers and aggregates tournaments.
        """
        tournaments = []

        for source in self.sources:
            try:
                print(f"Scraping from {source.__class__.__name__}...")
                result = source.scrape()
        
                tournaments.extend(result)
            except Exception as e:
                print(f"Error in {source.__class__.__name__}: {e}")

        return tournaments

    def save_to_database(tournaments):
        repo = TournamentRepository()
            
        tournaments.sort(key=lambda t: t.tournament_date)
    
        for t in tournaments:
            existing = repo.find_existing(t.name, t.tournament_date)
    
            if existing:
                tournament_id, existing_sources = existing
    
                # Merge sources
                merged_sources = list(set(existing_sources + t.source))
    
                t.source = merged_sources
                t.update_timestamp()
    
                repo.update(tournament_id, t)
    
                print(f"Updated: {t.name}")
    
            else:
                repo.insert(t)
                print(f"Inserted: {t.name}")

if __name__ == "__main__":
    scraper = MainScraper()
    tournaments = scraper.scrap_data()

    print(f"\nTotal tournaments scraped: {len(tournaments)}\n")

    for t in tournaments:
        print(t)
