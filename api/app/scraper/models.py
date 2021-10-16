from bs4 import (
    BeautifulSoup,
    Tag
)
from abc import abstractmethod
from functools import lru_cache

class Component: 

    def __init__(self, soup):
        self.soup = soup

    @lru_cache()
    def __call__(self):
        return self.find()
    
    @abstractmethod
    def find(self):
        return

class ScraperModel:

    DB_MODEL = None

    def __init__(self, soup):
        self.soup = soup

    def init_fields(self):
        curr_fields = [elem for elem in self.__dict__.items()]
        for attr, v in curr_fields:
            if attr.startswith('_') and isinstance(v, Component):
                setattr(self, attr.lstrip('_'), v.find())

    def to_dict(self):
        res = {}
        for attr, v in self.__dict__.items():
            if isinstance(v, Component):
                component_name = attr.lstrip('_')
                res[component_name] = getattr(self, component_name)
        return res

    def to_db_model(self):
        dic = self.to_dict()
        model = self.DB_MODEL(**dic)
        return model

class Price(Component):

    def find(self):
        price = self.soup.find('span', {'class': 'price'})
        if price: 
            return int(price.string.lstrip('$'))

class Title(Component):

    def find(self):
        return self.soup.title.string

class Description(Component):

    def find(self):
        desc_section = self.soup.find('section', id='postingbody')
        if desc_section: 
            return desc_section.get_text().rstrip().split('\n')[-1]

class Tags(Component):

    def find(self):
        res = {}
        for child in self.soup.find('p', {'class': 'attrgroup'}):
            if not isinstance(child, Tag) or not child.text:
                continue
            split_text = child.text.split(':')
            if len(split_text) == 1:
                tag = split_text[0]
                val = True
            else:
                tag, val = split_text
                val = val.lstrip()
            res[tag] = val
        return res

class Longitude(Component):

    def find(self):
        longitude = self.soup.find('div', id='map')
        if longitude:
            return longitude.attrs.get('data-longitude')

class Latitude(Component):

    def find(self):
        latitude = self.soup.find('div', id='map')
        if latitude:
            return latitude.attrs.get('data-latitude')

class PictureURL(Component):

    def find(self):
        img = soup.find('img')
        if img:
            return img.attrs.get('src')
            
class FurnitureScraperModel(ScraperModel):

    def __init__(self, soup):
        super().__init__(soup)
        self._price = Price(soup)
        self._title = Title(soup)
        self._description = Description(soup)
        self._tags = Tags(soup)
        self._longitude = Longitude(soup)
        self._latitude = Latitude(soup)
        self._picture_url = PictureURL(soup)
        self.init_fields()
