from src.core.application.result_handlers.result import Result
from src.kid_records.domain.repository.record_repository import Record_repository
from src.core.application.application_service import ApplicationService
from bson import Binary


class find_one_kid_record_service[str, dict](ApplicationService):
    
    kid_record_repository: Record_repository
    
    def __init__(self,record_repository):
        super().__init__()
        self.kid_record_repository = record_repository
    
    async def execute(self,id: str) -> dict:
        response: Result = await self.kid_record_repository.find_one(id)          
        #if response.is_error():
        #     return {'Error': response.get_error_message()}
        return response

        
        
    