from commons.application.application_service import ApplicationService

class LoggingDecorator[TService,TRespond](ApplicationService):

    decoratee: ApplicationService

    def __init__(self, logger, decoratee):
        pass

    def execute(TService) -> TRespond:
        pass
