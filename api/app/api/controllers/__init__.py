from flask import Blueprint
from flask_restx import Api

from .hello_world_controller import hello_world_controller
from .exporter_controller import exporter_controller
from .query_controller import query_controller

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp,
    title='Klarity API',
    version='1.0',
    validate=False
)
api.add_namespace(hello_world_controller)
api.add_namespace(exporter_controller)
api.add_namespace(query_controller)