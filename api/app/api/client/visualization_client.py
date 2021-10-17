import pandas as pd

from collections import defaultdict
from functools import lru_cache

class VisualizationClient:

    def __init__(self, dao_lst):
        self.daos = [dao._data for dao in dao_lst]
    
    @property 
    @lru_cache()
    def df(self):
        return pd.DataFrame(self.daos)

    @property 
    @lru_cache()
    def df_date_groupby(self):
        return self.df.groupby(self.df['post_time'].dt.date)

    def create_groupby_json(self, df, viz_type):
        res = defaultdict(dict)
        for date, val in zip(df.index, df):
            res[str(date)][viz_type] = round(val, 2)
        return res

    def viz_median_price(self):
        df = self.df_date_groupby.median()['price']
        return self.create_groupby_json(df, 'median')
        
    def viz_mean_price(self):
        df = self.df_date_groupby.mean()['price']
        return self.create_groupby_json(df, 'mean')

    def viz_max_price(self):
        df = self.df_date_groupby.max()['price']
        return self.create_groupby_json(df, 'max')

    def viz_min_price(self):
        df = self.df_date_groupby.min()['price']
        return self.create_groupby_json(df, 'min')



        
        

            

    

    

    
        