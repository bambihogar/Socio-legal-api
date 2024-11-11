from src.core.application.result_handlers.result import Result
from src.kid_records.domain.repository.record_repository import Record_repository
from src.core.application.application_service import ApplicationService
from src.kid_records.application.commands.create.types.dto import Create_kid_record_dto

class Create_kid_record_service[Create_kid_record_dto, dict](ApplicationService):
    kid_record_repository: Record_repository
    
    def __init__(self,record_repository,uuid):
        super().__init__()
        self.kid_record_repository = record_repository
        self.uuid = uuid
    
    async def execute(self,dto: Create_kid_record_dto):
        response = await self.kid_record_repository.create_kid_record(dto)
        #if response.is_error():
        #    return response
        return response
        
        

    