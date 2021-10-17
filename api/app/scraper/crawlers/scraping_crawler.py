import requests

from bs4 import BeautifulSoup

from .crawler import Crawler
from ..models.furniture import FurnitureScraperModel
from ...shared.models.furniture import FurnitureDAO
from ...api.exceptions import ApiError
from ...labeller.client import LabelerClient

class ScrapingCrawler(Crawler):

    def __init__(self, base_url, client):
        super().__init__(base_url)
        self.labeller = client

    def scrape(self):
        if self.check_in_db(self.base_url):
            return
        try:
            html = self.get_html(self.base_url)
            soup = self.get_soup(html)
            if soup.title.string:
                print(self.base_url, flush=True)
                furniture = FurnitureScraperModel(soup, self.base_url)
                furniture = self.labeller.label(furniture)
                furniture.save_to_db()
        except Exception as e:
            raise ApiError(
                f"Request failed for {self.base_url}"
            )
    
    def check_in_db(self, url):
        return FurnitureDAO.objects(url=url)