from fastapi import FastAPI
from src.kid_records.infrastructure.routes.kid_records_routes import kid_records_router
import os

application = FastAPI()
application.include_router(kid_records_router)
