from src.core.application.result_handlers.result import Result
from src.kid_records.domain.repository.record_repository import Record_repository
from src.core.application.application_service import ApplicationService


class Delete_kid_record_service[str,dict](ApplicationService):
    def __init__(self, kid_record_repository: Record_repository):
        super().__init__()
        self.kid_record_repository = kid_record_repository

    async def execute(self, id):
        response: Result = await self.kid_record_repository.delete_record(id)
        if response.is_error():
            return {'Error': response.get_error_message()}
        return response.develop()