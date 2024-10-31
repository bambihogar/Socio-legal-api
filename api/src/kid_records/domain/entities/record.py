from datetime import datetime 
from typing import List

class record:
    id_record: str
    court_record_id: str
    bambi_entry_date: List[datetime]
    bambi_entry_reasons : List[str]
    bambi_exit_date: List[datetime]
    bambi_exit_reasons: List[str]
    justice_organization: str

    def __init__(
            self,
            id:str, 
            court_record_id:str, 
            entry_date:str, 
            entry_reasons:str, 
            exit_date:str, 
            exit_reasons:str,
            organization:str
        ):
        self.id = id
        self.court_record_id = court_record_id
        self.bambi_entry_date = entry_date
        self.bambi_entry_reasons = entry_reasons
        self.bambi_exit_date = exit_date
        self.bambi_exit_reasons = exit_reasons
        self.justice_organization = organization