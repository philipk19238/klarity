import requests
import random

from bs4 import BeautifulSoup
from abc import abstractmethod

class Crawler:

    USER_AGENT_LIST = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def scrape(self):
        pass

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def get_html(self, url):
        req = requests.get(url, headers={'User-Agent': self.random_agent()})
        if req.status_code == 200:
            return req.text

    def random_agent(self):
        idx = random.randint(0, len(self.USER_AGENT_LIST) - 1)
        return self.USER_AGENT_LIST[idx]
