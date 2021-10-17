from ..crawlers.scraping_crawler import ScrapingCrawler
from .pipeline import Pipeline

class ScrapingPipeline(Pipeline):

    def _scrape(self, url):
        crawler = ScrapingCrawler(url)
        crawler.scrape()