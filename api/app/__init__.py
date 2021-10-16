import os

from flask import Flask
from .controllers import api

from .extensions import (
    db, 
    cors
)

from .global_config import Config

def register_extensions(app) -> None: 
    api.init_app(app)
    db.init_app(app)
    cors.init_app(app)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app) 
    
    return app
