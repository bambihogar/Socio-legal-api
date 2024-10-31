from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    MONGO_HOST = "localhost" 
    MONGO_PORT = "27018"
    MONGO_DB = "bambi_socio_legal"
    MONGO_USER = "root"
    MONGO_PASS = "secret"

    class Config:
        env_file = './.env'


settings = Settings()