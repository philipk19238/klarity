import os

from flask import Flask, url_for

from .global_config import Config

def register_extensions(app) -> None: 
    from .extensions import (
        db, 
        cors
    )
    from .scraper.controllers import scraper

    scraper.init_app(app)
    db.init_app(app)
    cors.init_app(app)

def register_api(app):
    from .api.controllers import api_bp
    
    app.register_blueprint(api_bp)
    
def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    register_api(app)
    register_extensions(app) 

    print(app.url_map, flush=True)
    
    return app
