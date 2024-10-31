from fastapi import APIRouter, Depends, FastAPI
from src.kid_records.infrastructure.repositories.mongo_record_repository import Mongo_record_repository
from src.kid_records.application.queries.find_one.find_one_kid_record import find_one_kid_record_service
from src.kid_records.application.commands.update.update_kid_record import Update_kid_record_service
from src.kid_records.application.commands.create.create_kid_record import Create_kid_record_service
from src.core.infrastructure.config.database import get_db
from src.kid_records.infrastructure.routes.entries.create_kid_record_entry import Create_kid_record_entry
from uuid import uuid4

kid_records_router = APIRouter(
    prefix="/kid_record",
    tags=["kid_record"],
    responses={404: {"description": "Not found"}},
)

kid_record_repository = Mongo_record_repository() 


@kid_records_router.post("/",)
async def create(
        body: Create_kid_record_entry):
    #kid_record_repository = Mongo_record_repository() 
    service =  Create_kid_record_service(kid_record_repository,uuid4)
    result = await service.execute(body) 
    print(result)
    
    return result


@kid_records_router.get("/find_one/{id}",)
async def find_one(id:str):
        service =  find_one_kid_record_service(kid_record_repository)
        result = await service.execute(id)
        print('en route: ',result)
        return result

@kid_records_router.get("/search/",)
async def search():
    return {"username": "search"}



@kid_records_router.patch("/update/",)
async def update(
     body: Create_kid_record_entry, 
     DB = Depends(get_db)
     ):
    kid_records = DB['kid_information']
    service = Update_kid_record_service(kid_records,uuid4)
    result = await service.execute(body) 
    print(result)
    return {"username": "update"}


@kid_records_router.delete("/create",)
async def delete():
    return {"username": "delete"}





