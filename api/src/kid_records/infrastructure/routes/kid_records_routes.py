from fastapi import APIRouter, FastAPI
from src.kid_records.infrastructure.routes.entries.create_kid_record_entry import Create_kid_record_entry
from src.kid_records.infrastructure.routes.entries.update_kid_record_entry import Update_kid_record_entry
from src.kid_records.infrastructure.repositories.mongo_record_repository import Mongo_record_repository
from src.kid_records.application.queries.find_one.find_one_kid_record import find_one_kid_record_service
from src.kid_records.application.commands.update.update_kid_record import Update_kid_record_service
from src.kid_records.application.commands.create.create_kid_record import Create_kid_record_service
from src.kid_records.application.commands.update.types.dto import Update_kid_record_dto
from uuid import uuid4

kid_records_router = APIRouter(
    prefix="/kid_record",
    tags=["kid_record"],
    responses={404: {"description": "Not found"}},
)

kid_records_repository = Mongo_record_repository() 


@kid_records_router.post("/",)
async def create(
        body: Create_kid_record_entry):
    service =  Create_kid_record_service(kid_records_repository,uuid4)
    result = await service.execute(body) 
    return result


@kid_records_router.get("/{id}",)
async def find_one(id:str):
    service =  find_one_kid_record_service(kid_records_repository)
    result = await service.execute(id)
    return result

@kid_records_router.get("/",)
async def search():
    return {"username": "search"}



@kid_records_router.put("/{id}/",)
async def update(body: Update_kid_record_entry, id: str):
    dto = organize_update_dto(body,id)
    service = Update_kid_record_service(kid_records_repository)
    result = await service.execute(dto) 
    return result


@kid_records_router.delete("/create",)
async def delete():
    return {"username": "delete"}




def organize_update_dto(entry: Update_kid_record_entry, id:str)->Update_kid_record_dto:
    dto = Update_kid_record_dto(
         id =id,
         kid_internal_id = entry.kid_internal_id,
         kid_last_names = entry.kid_last_names,
         kid_names = entry.kid_names,
         kid_personal_id = entry.kid_personal_id,
         kid_birth_certificate = entry.kid_birth_certificate,
         record_court_id = entry.record_court_id,
         record_bambi_entry_date=entry.record_bambi_entry_date,
         record_bambi_entry_reasons=entry.record_bambi_entry_reasons,
         record_bambi_departure_date=entry.record_bambi_departure_date,
         record_bambi_departure_reason=entry.record_bambi_departure_reason,
         record_justice_organization=entry.record_justice_organization,
         responsible_names=entry.responsible_names,
         responsible_identification=entry.responsible_identification,
         responsible_contact=entry.responsible_contact
         )
    return dto
