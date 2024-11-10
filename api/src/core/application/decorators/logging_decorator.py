from src.core.application.result_handlers.result import Result
from src.core.application.application_service import ApplicationService

class LoggingDecorator[TService,TRespond](ApplicationService):

    decoratee: ApplicationService 
    def __init__(self, decoratee, logger):
        self.logger = logger
        self.decoratee = decoratee

    def execute(self,TService) -> TRespond:
        result:Result =self.decoratee.execute()
        if(result.is_error()):
            self.logger.log_error()
        if (result.is_succes()):
            self.logger.log_succes()
        return result    

            
