from scraper.base import (
    ScraperModel,
    Listings
)

class PageScraperModel(ScraperModel):

    def __init__(self, soup):
        self._listings = Listings(soup)
        super().__init__(soup)
