from nltk.corpus import stopwords

from ..crawlers.scraping_crawler import ScrapingCrawler
from .pipeline import Pipeline
from ...labeller.client import LabelerClient

class ScrapingPipeline(Pipeline):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stopwords = set(stopwords.words("english"))
        self.client = LabelerClient(self.stopwords)

    def _scrape(self, url):
        crawler = ScrapingCrawler(url, self.client)
        crawler.scrape()
