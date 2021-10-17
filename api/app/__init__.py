import os

from flask import Flask

from .global_config import Config

def register_extensions(app) -> None: 
    from .extensions import (
        db, 
        cors
    )
    db.init_app(app)
    cors.init_app(app)

def register_api(app):
    from .api.controllers import api_bp
    from .scraper.controllers import scraper_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(scraper_bp)
    
def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    register_api(app)
    register_extensions(app) 
    
    return app
