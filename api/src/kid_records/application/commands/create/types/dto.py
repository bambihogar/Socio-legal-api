from pydantic import BaseModel, Field
from datetime import datetime  
from typing import List

class Create_kid_record_dto(BaseModel):
        kid_internal_id: str = Field(...,min_length=4)
        kid_last_names: str = Field(..., min_length=3)
        kid_names: str = Field(...,min_length=3)
        kid_personal_id: str | None  
        kid_birth_certificate: str | None       
        record_court_id: str = Field(...,min_length=4)
        record_bambi_entry_date: List[datetime] = Field(...)
        record_bambi_entry_reasons: List[str] = Field(...) 
        record_bambi_departure_date: List[datetime] | None
        record_bambi_departure_reason: List[str] | None
        record_justice_organization: str = Field(...,min_length=5)      
        responsible_names: list[str] | None
        responsible_identification:list[str] | None
        responsible_contact:list[str] | None
