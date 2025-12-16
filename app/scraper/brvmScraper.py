import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

class BrvmScraper:
    def scrape_indices(self):
        url = "https://www.brvm.org/fr/indices"
        response = requests.get(url, timeout=10,verify=False)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        indices = {}

        tables = soup.find_all("table")
       
        for table in tables:
            rows = table.find_all("tr")
            for row in rows[1:]:
                cols = row.find_all("td")
                if len(cols) >= 3:
                    name = cols[0].get_text(strip=True)

                if name.startswith("BRVM"):
                    indices[name] = {
                    "value": cols[1].get_text(strip=True),
                    "variation": cols[2].get_text(strip=True)
                }

        return indices

    def scrape_stocks(self):
        url = "https://www.brvm.org/fr/cours-actions/0"
        stocks = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=60000)

            page.wait_for_selector("table tbody tr", timeout=60000)

            rows = page.query_selector_all("table tbody tr")

            for row in rows:
                cols = row.query_selector_all("td")
                if len(cols) >= 5:
                    stocks.append({
                        "symbol": cols[0].inner_text().strip(),
                        "company": cols[1].inner_text().strip(),
                        "price": cols[2].inner_text().strip(),
                        "variation": cols[3].inner_text().strip(),
                        "volume": cols[4].inner_text().strip(),
                    })

            browser.close()

        return stocks
