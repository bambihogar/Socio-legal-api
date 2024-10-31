from src.kid_records.domain.repository.record_repository import Record_repository
from src.core.application.application_service import ApplicationService
from bson import Binary


class find_one_kid_record_service[str, dict](ApplicationService):
    
    kid_record_repository: Record_repository
    
    def __init__(self,record_repository):
        super().__init__()
        self.kid_record_repository = record_repository
    
    async def execute(self,id: str) -> dict:
        try:
            kid_record = await self.kid_record_repository.find_one(id)
            print('kid_record en service', kid_record)
            
            print()
            return kid_record

        except Exception as e:
            print(e)    
        
        
        
    