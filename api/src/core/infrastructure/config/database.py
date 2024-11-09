from pymongo import MongoClient

MONGO_HOST = "localhost" 
MONGO_PORT = "27018"
MONGO_DB = "bambi_socio_legal"
MONGO_USER = "root"
MONGO_PASS = "secret"

def get_db():
    uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
    client = MongoClient(uri)
    database = client['bambi_socio_legal']
    kids = database['kid_information']
    
    return kids




