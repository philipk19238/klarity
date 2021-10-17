from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
from abc import abstractmethod

class Pipeline:

    def __init__(self, urls):
        self.urls = urls
        self.cpu_count = cpu_count()

    def scrape(self):
        pool = Pool(self.cpu_count)
        func = self._scrape
        return pool.map(func, self.urls)

    @abstractmethod
    def _scrape(self):
        pass
        

