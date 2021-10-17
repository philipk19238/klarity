import requests

from flask_restx import Namespace, Resource
from ..pipelines.scraping_pipeline import ScrapingPipeline
from ..pipelines.seeding_pipeline import SeedingPipeline
from ...shared.models.link import LinkDAO
from ...shared.models.furniture import FurnitureDAO
from bs4 import BeautifulSoup
from ...labeller.client import LabelerClient

scraper_controller = Namespace(
    'Scraper', 'Scraper endpoint', '/scraper')

@scraper_controller.route('/scrape')
class ScraperController(Resource):

    @scraper_controller.response(201, 'Successfully scraped link data')
    def get(self):
        page = LinkDAO.objects.paginate(page=3, per_page=100)
        while page.has_next:
            urls = [obj.link for obj in page.items]
            pipeline = ScrapingPipeline(urls)
            pipeline.scrape()
            page = page.next()

@scraper_controller.route('/seed')
class SeedController(Resource):

    @scraper_controller.response(201, 'Successfully seeded database with links')
    def get(self):
        pipeline = SeedingPipeline()
        pipeline.scrape()






            

