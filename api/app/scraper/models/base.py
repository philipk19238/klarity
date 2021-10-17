from bs4 import (
    BeautifulSoup,
    Tag
)
from abc import abstractmethod
from functools import lru_cache
from datetime import datetime

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
        self.init_fields()

    def init_fields(self):
        curr_fields = [elem for elem in self.__dict__.items()]
        for attr, v in curr_fields:
            if attr.startswith('_') and isinstance(v, Component):
                setattr(self, attr.lstrip('_'), v.find())

    def to_dict(self):
        res = {}
        for attr, v in self.__dict__.items():
            if isinstance(v, Component):
                print(attr, v, flush=True)
                component_name = attr.lstrip('_')
                res[component_name] = getattr(self, component_name)
        return res

    def to_db_model(self):
        dic = self.to_dict()
        model = self.DB_MODEL(**dic)
        return model

class PostID(Component):

    def find(self):
        post_div = self.soup.find('div', {'class': 'postinginfos'})
        post_id = post_div.find('p')
        if post_id:
            return int(post_id.text.split()[-1])

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
        img = self.soup.find('img')
        if img:
            return img.attrs.get('src')

class PostTime(Component):

    def find(self):
        time = self.soup.find('time', {'class': 'date timeago'})
        if time:
            time_str = time.attrs.get('datetime')
            return datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S-%f')

class Listings(Component):

    def find(self):
        res = []
        for listing in self.soup.find_all('li', {'class': 'result-row'}):
            link = listing.find('a', {'class': ['result-title hdrlnk']}, href=True)
            if link:
                res.append(link.attrs['href'])
        return res
            

