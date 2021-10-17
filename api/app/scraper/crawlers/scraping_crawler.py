import requests

from bs4 import BeautifulSoup

from .crawler import Crawler
from ..models.furniture import FurnitureScraperModel

class ScrapingCrawler(Crawler):

    def scrape(self):
        print(self.base_url, flush=True)
        html = self.get_html(self.base_url)
        soup = self.get_soup(html)
        furniture = FurnitureScraperModel(soup)
        furniture.save_to_db()