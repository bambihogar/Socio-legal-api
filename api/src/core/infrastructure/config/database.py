from pymongo import MongoClient
from src.core.infrastructure.config.config import get_settings

env = get_settings()

def get_db(): 
    try:
        client = MongoClient(env.DB_CONNECTION)
        database = client['bambi_socio_legal']
        kids = database['kid_information']
        return kids
    except Exception as e:
        print(e)    



