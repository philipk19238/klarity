from .base import BaseDocument
from ...extensions import db

class FurnitureDAO(BaseDocument):
    meta = {'collection': 'scraped_items'}
    _id = db.IntField()
    price = db.FloatField()
    title = db.StringField()
    description = db.StringField()
    tags = db.DictField()
    longitude = db.FloatField()
    latitude = db.FloatField()
    picture_url = db.StringField()
    post_time = db.DateTimeField()
    url = db.StringField()
