import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

class Config: 
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGO_HOST')
    }

