from src.core.application.application_service import ApplicationService
from src.kid_records.application.queries.search.types.dto import Search_kid_dto
from src.kid_records.domain.repository.record_repository import Record_repository


class Search_kid_service[str, dict](ApplicationService):
    kid_record_repository: Record_repository

    def __init__(self,record_repository):
        super().__init__()
        self.kid_record_repository = record_repository
    
    async def execute(self, dto:Search_kid_dto) -> dict:
            kids = await self.kid_record_repository.search(dto)
            return kids
    
        