from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

migrate = Migrate(compare_type=True)
db = SQLAlchemy()
cors = CORS()