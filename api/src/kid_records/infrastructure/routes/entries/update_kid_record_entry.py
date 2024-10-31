from pydantic import BaseModel, Field
from datetime import datetime  
from typing import List

class Update_kid_record_entry(BaseModel):
        
        kid_last_names: str = Field(..., min_length=3) | None
        kid_names: str = Field(...,min_length=3) | None
        kid_personal_id: str = Field(min_length=8) | None
        kid_birth_certificate: str | None 

        record_court_id: str = Field(...,min_length=4) | None
        record_bambi_entry_date: List[datetime] = Field(...) | None
        record_bambi_entry_reasons: List[str] = Field(...) | None
        record_bambi_departure_date: List[datetime] | None
        record_bambi_departure_reason: List[str] | None
        record_justice_organization: str = Field(...,min_length=5) | None

        responsible_names: list[str] | None
        responsible_identification:list[str] | None
        responsible_contact:list[str] | None
        

