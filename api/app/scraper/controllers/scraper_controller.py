import requests

from flask_restx import Namespace, Resource
from ..models.furniture import FurnitureScraperModel
from bs4 import BeautifulSoup

scraper_controller = Namespace(
    'Scraper', 'Scraper endpoint', ''
)

@scraper_controller.route('/scrape')
class ScraperController(Resource):
     
     @scraper_controller.response(201, 'Successfully scraped data')
     def get(self):
         soup = BeautifulSoup(requests.get('https://collegestation.craigslist.org/fuo/d/twin-size-mattress-and-box-spring/7393912311.html').text, 'html.parser')
         scraper_model = FurnitureScraperModel(soup)
         db_model = scraper_model.to_db_model()
         db_model.save()
         