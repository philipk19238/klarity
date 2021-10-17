from .base import (
    ScraperModel,
    Listings
)
from ...shared.models.link import LinkDAO

from functools import lru_cache

class PageScraperModel(ScraperModel):

    DB_MODEL = LinkDAO

    def __init__(self, soup, cursor, max_cursor=None):
        self._listings = Listings(soup)
        self.cursor = cursor
        self._max_cursor = max_cursor
        super().__init__(soup)

    @property 
    def next_cursor(self):
        if self.max_cursor - self.cursor >= 120:
            return self.cursor + 120

    @property 
    @lru_cache()
    def max_cursor(self):
        if self._max_cursor is None:
            max_cursor = self.soup.find('span', {'class': 'totalcount'})
            return int(max_cursor.text)
        else:
            return self._max_cursor

    @lru_cache()
    def save_to_db(self):
        res = []
        for listing in self.listings:
            kwargs = {'_id': listing, 'link': listing}
            res.append(self.DB_MODEL(**kwargs))
        LinkDAO.objects.insert(res)