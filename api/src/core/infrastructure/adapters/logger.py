import logging
from src.core.application.log import Logger

#"/../../../kid_record_log.log"
class Log_Python(Logger):
    
    def __init__(self,route):
        logging.basicConfig(
            level=logging.INFO,
            #filename=route, 
            #filemode="w", 
            #encoding='utf-8',
            format="%(asctime)s - %(levelname)s - %(message)s"
            )
        print('route')
    
    def log_succes(self,info: str):
        logging.info(info)
    
    def log_failure(self,error: str):
        logging.error(error)