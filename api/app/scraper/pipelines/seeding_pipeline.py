from ..crawlers.seeding_crawler import SeedingCrawler
from .pipeline import Pipeline

class SeedingPipeline(Pipeline):

    def _scrape(self, url):
        crawler = SeedingCrawler(url)
        crawler.scrape()