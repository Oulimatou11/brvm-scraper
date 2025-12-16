from app.scraper.brvmScraper import BrvmScraper

class MarketService:

    def __init__(self):
        self.scraper = BrvmScraper()

    def get_indices(self):
        return self.scraper.scrape_indices()

    def get_stocks(self):
        return self.scraper.scrape_stocks()

    def refresh_data(self):
        self.indices = self.scraper.scrape_indices()
        self.stocks = self.scraper.scrape_stocks()