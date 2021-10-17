import requests

from bs4 import BeautifulSoup

from .crawler import Crawler
from ..models.page import PageScraperModel

class SeedingCrawler(Crawler):

    def __init__(self, base_url):
        super().__init__(base_url + '/d/furniture/search/fua?')
        self.stack = []

    def scrape(self):
        html = self.get_html(self.base_url)
        soup = self.get_soup(html)
        self.stack.append(
            PageScraperModel(
                soup,
                0
            )
        )
        self._dfs()

    def _dfs(self):
        while self.stack:
            node = self.stack.pop()
            if node.next_cursor:
                url = self.get_next_url(node.next_cursor)
                print(url, flush=True)
                html = self.get_html(url)
                soup = self.get_soup(html)
                self.stack.append(
                    PageScraperModel(
                        soup,
                        node.next_cursor,
                        node.max_cursor
                    )
                )
                node.save_to_db()

    def get_next_url(self, next_cursor):
        return self.base_url + f's={next_cursor}'

    def get_html(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            return req.text

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')
