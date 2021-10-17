import pandas as pd
import json

from flask_restx import Namespace, Resource
from flask import request
from collections import defaultdict

from ...shared.models.furniture import FurnitureDAO
from ..client.query_client import QueryClient
from ..client.visualization_client import VisualizationClient

query_controller = Namespace(
    'Query', 'Query endpoint', '/query')

query_client = QueryClient([
    'type',
    'condition',
    'material',
    'home_location',
    'color',
    'mattress_size'
])

@query_controller.route('/<viz_type>')
class QueryController(Resource):

    @query_controller.response(200, 'Successfully queried data')
    def get(self, viz_type):
        parsed = query_client.parse_request(request, subtarget='tags')
        res = query_client.query(FurnitureDAO, **parsed)
        viz_client = VisualizationClient(res)
        res = {}
        if viz_type == 'median':
            res['median'] = viz_client.viz_median_price()
        elif viz_type == 'mean':
            res['mean'] = viz_client.viz_mean_price()
        elif viz_type == 'min':
            res['min'] = viz_client.viz_min_price()
        elif viz_type == 'max':
            res['max'] = viz_client.viz_max_price()
        res['viz_type'] = viz_type
        res['params'] = parsed
        return res

            
            
            
        




                
        
            


        


