from .base import BaseDocument
from ...extensions import db

class LinkDAO(BaseDocument):
    meta = {'collection': 'seed_links'}
    _id = db.StringField()
    link = db.StringField()
