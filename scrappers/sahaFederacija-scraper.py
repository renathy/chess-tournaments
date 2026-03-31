from playwright.sync_api import sync_playwright
from models.tournament import Tournament

class SahaFederacijaScraper:
    SOURCE_NAME = "sahafederacija"
    BASE_URL = "https://play.sahafederacija.lv/tournaments"

    def scrape(self):
        tournaments = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(self.BASE_URL, timeout=60000)

            # Wait for table/list to load
            page.wait_for_selector("table")

            # --- Pagination loop ---
            while True:
                rows = page.query_selector_all("table tbody tr")

                for row in rows:
                    cols = row.query_selector_all("td")

                    if not cols:
                        continue

                    try:
                        name = cols[0].inner_text().strip()
                        date = cols[1].inner_text().strip()

                        tournament = Tournament(
                            name=name,
                            tournament_date=date,
                            source=[self.SOURCE_NAME],
                        )

                        tournaments.append(tournament)

                    except Exception as e:
                        print(f"Row parsing error: {e}")

                next_button = page.query_selector("button:has-text('Next')")

                if not next_button or "disabled" in next_button.get_attribute("class"):
                    break

                next_button.click()
                page.wait_for_timeout(1500)

            browser.close()

        return tournaments
