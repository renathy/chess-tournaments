from scrapers.saha_federacija import SahaFederacijaScraper

class MainScraper:
    def __init__(self):
        self.sources = self._load_sources()

    def _load_sources(self):
        """
        Register all scraper sources here.
        """
        return [
            SahaFederacijaScraper(),
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

if __name__ == "__main__":
    scraper = MainScraper()
    tournaments = scraper.scrap_data()

    print(f"\nTotal tournaments scraped: {len(tournaments)}\n")

    for t in tournaments:
        print(t)
