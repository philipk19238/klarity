from flask import Blueprint
from flask_restx import Api
from .scraper_controller import scraper_controller

scraper_bp = Blueprint('scraper', __name__, url_prefix='/scraper')
scraper = Api(scraper_bp,
        title='Scraper Jobs',
        version='1.0'
)
scraper.add_namespace(scraper_controller)