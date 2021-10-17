from flask_restx import Api
from .scraper_controller import scraper_controller

scraper = Api(
    title='Scraper Jobs',
    version='1.0'
)
scraper.add_namespace(scraper_controller)