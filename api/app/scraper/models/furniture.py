from .base import (
    ScraperModel,
    Price,
    Title,
    Description,
    Tags,
    Longitude,
    Latitude,
    PictureURL,
    PostTime,
    PostID
)
from ...shared.models.furniture import FurnitureDAO

class FurnitureScraperModel(ScraperModel):

    DB_MODEL = FurnitureDAO

    def __init__(self, soup, url):
        self.url = url
        self._id = PostID(soup)
        self._price = Price(soup)
        self._title = Title(soup)
        self._description = Description(soup)
        self._tags = Tags(soup)
        self._longitude = Longitude(soup)
        self._latitude = Latitude(soup)
        self._picture_url = PictureURL(soup)
        self._post_time = PostTime(soup)
        super().__init__(soup)

    def to_dict(self):
        res = super().to_dict()
        res['_id'] = res['id']
        res['url'] = self.url
        del res['id']
        return res
