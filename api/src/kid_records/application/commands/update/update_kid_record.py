from src.core.application.result_handlers.result import Result
from src.kid_records.domain.repository.record_repository import Record_repository
from src.core.application.application_service import ApplicationService
from src.kid_records.application.commands.update.types.dto import Update_kid_record_dto

class Update_kid_record_service[Update_kid_record_dto, dict](ApplicationService):
    
    def __init__(self,kid_record_repository: Record_repository ):
        super().__init__()
        self.kid_record_repository = kid_record_repository
    
    async def execute(self,dto: Update_kid_record_dto) -> dict:
        response:Result = await self.kid_record_repository.modify_record(dto)
        #if response.is_error():
        #        return {'Error': response.get_error_message()}
        return response
    