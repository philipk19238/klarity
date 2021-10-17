from ..crawlers.seeding_crawler import SeedingCrawler
from .pipeline import Pipeline

STARTING_URLS = [
    "http://atlanta.craigslist.org/",
    "http://austin.craigslist.org/",
    "http://boston.craigslist.org/",
    "http://chicago.craigslist.org/",
    "http://dallas.craigslist.org/",
    "http://denver.craigslist.org/",
    "http://detroit.craigslist.org/",
    "http://houston.craigslist.org/",
    "http://lasvegas.craigslist.org/",
    "http://losangeles.craigslist.org/",
    "http://miami.craigslist.org/",
    "http://minneapolis.craigslist.org/",
    "http://newyork.craigslist.org/",
    "http://orangecounty.craigslist.org/",
    "http://philadelphia.craigslist.org/",
    "http://phoenix.craigslist.org/",
    "http://portland.craigslist.org/",
    "http://raleigh.craigslist.org/",
    "http://sacramento.craigslist.org/",
    "http://sandiego.craigslist.org/",
    "http://seattle.craigslist.org/",
    "http://sfbay.craigslist.org/",
    "http://washingtondc.craigslist.org/"
]

class SeedingPipeline(Pipeline):

    def __init__(self):
        super().__init__(STARTING_URLS)

    def _scrape(self, url):
        crawler = SeedingCrawler(url)
        crawler.scrape()
