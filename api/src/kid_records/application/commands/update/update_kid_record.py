from src.core.application.application_service import ApplicationService
from src.kid_records.application.commands.update.types.dto import Update_kid_record_dto
from bson import Binary

class Update_kid_record_service[Update_kid_record_dto, dict](ApplicationService):
    
    def __init__(self,kid_record_collection, schema):
        super().__init__()
        self.kid_record_collection = kid_record_collection
        self.schema = schema
    
    async def execute(self,dto: Update_kid_record_dto) -> dict:
        
        exe = self.ensamble_kid_record(dto,self.uuid())
        document = self.kid_record_collection.insert_one(exe)
        print(document)
        return 'hola mundo'

    