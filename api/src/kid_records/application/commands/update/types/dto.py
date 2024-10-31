from pydantic import BaseModel, Field
from datetime import datetime  
from typing import List

class Update_kid_record_dto(BaseModel):
    kid_last_names: str = Field(..., min_length=3)
    kid_names: str = Field(...,min_length=3) 
    kid_personal_id: str = Field(min_length=8) 
    kid_birth_certificate: str 

    record_court_id: str = Field(...,min_length=4) 
    record_bambi_entry_date: List[datetime] = Field(...) 
    record_bambi_entry_reasons: List[str] = Field(...) 
    record_bambi_departure_date: List[datetime] 
    record_bambi_departure_reason: List[str] 
    
    record_justice_organization: str = Field(...,min_length=5)
    responsible_names: list[str] 
    responsible_identification:list[str] 
    responsible_contact:list[str] 
        

