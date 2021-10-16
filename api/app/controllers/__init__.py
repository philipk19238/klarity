from flask_restx import Api

from .hello_world_controller import hello_world_controller

api = Api(title='Klarity API', version='1.0', validate=True)

api.add_namespace(hello_world_controller)
