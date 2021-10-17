import requests

from flask_restx import Namespace, Resource
from ..pipelines.scraping_pipeline import ScrapingPipeline
from ...shared.models.link import LinkDAO
from bs4 import BeautifulSoup

scraper_controller = Namespace(
    'Scraper', 'Scraper endpoint', ''
)

@scraper_controller.route('/scrape')
class ScraperController(Resource):
     
     @scraper_controller.response(201, 'Successfully scraped data')
     def get(self):
         urls = [obj.link for obj in LinkDAO.objects]
         pipeline = ScrapingPipeline(urls)
         pipeline.scrape()