from bs4 import BeautifulSoup
from abc import abstractmethod

class Crawler:

    def __init__(self, base_url):
        self.base_url = base_url + '/d/furniture/search/fua?'

    @abstractmethod
    def scrape(self):
        pass

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def get_html(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            return req.text
