from src.core.infrastructure.adapters.logger import Log_Python
from src.core.application.decorators.logging_decorator import LoggingDecorator
from src.kid_records.application.commands.delete.delete_kid_record import Delete_kid_record_service
from src.kid_records.application.queries.search.types.dto import Search_kid_dto
from src.kid_records.application.queries.search.search_kid import Search_kid_service
from src.kid_records.application.queries.find_one.find_one_kid_record import find_one_kid_record_service
from src.kid_records.application.commands.update.update_kid_record import Update_kid_record_service
from src.kid_records.application.commands.create.create_kid_record import Create_kid_record_service
from src.kid_records.application.commands.update.types.dto import Update_kid_record_dto
from src.kid_records.infrastructure.routes.entries.update_kid_record_entry import Update_kid_record_entry
from src.kid_records.infrastructure.routes.entries.create_kid_record_entry import Create_kid_record_entry
from src.kid_records.infrastructure.routes.entries.search_kid_entry import Search_kid_entry
from src.kid_records.infrastructure.repositories.mongo_record_repository import Mongo_record_repository
from fastapi import APIRouter, FastAPI
from uuid import uuid4

kid_records_router = APIRouter(
    prefix="/kid_record",
    tags=["kid_record"],
    responses={404: {"description": "Not found"}},
)

kid_records_repository = Mongo_record_repository() 
logger = Log_Python("kid_record_log.log")

@kid_records_router.post("/",)
async def create(
        body: Create_kid_record_entry):
    service = LoggingDecorator(
          Create_kid_record_service(kid_records_repository,uuid4)
          ,logger)
    result = await service.execute(body) 
    return result


@kid_records_router.get("/{id}",)
async def find_one(id:str):
    service = LoggingDecorator(
          find_one_kid_record_service(kid_records_repository)
          ,logger)
    result = await service.execute(id)
    return result

@kid_records_router.get("/",)
async def search(q: str = None, page: int = 0, limit: int = 10):
        print(q,page,limit)
        if(q is None):
              return {'code':400,'msg':'You need to send real words to find records'}
        
        dto = Search_kid_dto(page= page,per_page=limit, search=q)
        service = LoggingDecorator(
          Search_kid_service(kid_records_repository)
          ,logger)
        result = await service.execute(dto)
        return result


@kid_records_router.put("/{id}/",)
async def update(body: Update_kid_record_entry, id: str):
        dto = organize_update_dto(body,id)
        service = LoggingDecorator(
          Update_kid_record_service(kid_records_repository)
          ,logger)
        result = await service.execute(dto) 
        return result
    

@kid_records_router.delete("/delete/{id}",)
async def delete(id:str):
        
        service = LoggingDecorator(
          Delete_kid_record_service(kid_records_repository)
          ,logger)
        result = await service.execute(id)
        return result




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
