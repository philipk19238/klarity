import requests

from flask_restx import Namespace, Resource
from ..crawlers.seeding_crawler import SeedingCrawler
from ..models.furniture import FurnitureScraperModel
from bs4 import BeautifulSoup

scraper_controller = Namespace(
    'Scraper', 'Scraper endpoint', ''
)

@scraper_controller.route('/scrape')
class ScraperController(Resource):
     
     @scraper_controller.response(201, 'Successfully scraped data')
     def get(self):
         crawler = SeedingCrawler('https://collegestation.craigslist.org')
         crawler.scrape()
         