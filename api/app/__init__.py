import os

from flask import Flask
from .controllers import api

from .extensions import (
    db, 
    migrate,
    cors
)

from .global_config import Config

def register_extensions(app) -> None: 
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app) 
    
    return app
