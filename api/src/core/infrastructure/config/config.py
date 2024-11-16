from pydantic_settings import BaseSettings
from functools import lru_cache



class Settings(BaseSettings):
    MONGO_HOST:str
    MONGO_PORT:str
    MONGO_DB:str 
    MONGO_USER:str
    MONGO_PASS:str
    DB_CONNECTION:str
    DB_CONNECTION_COMPOSE: str
    DB_CONNECTION_REMOTE: str

    class Config:
        pass


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
