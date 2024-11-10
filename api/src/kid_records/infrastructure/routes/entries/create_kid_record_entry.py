from pydantic import BaseModel, Field
from datetime import datetime  
from typing import List, Optional

class Create_kid_record_entry(BaseModel):
        kid_internal_id: str = Field(...,min_length=4)
        kid_last_names: str = Field(..., min_length=2)
        kid_names: str = Field(...,min_length=2)
        kid_personal_id: Optional[str] = Field(...,min_length=8)
        kid_birth_certificate: Optional[str] = Field(...,min_length=5)

        record_court_id: str = Field(...,min_length=4)
        record_bambi_entry_date: List[datetime] = Field(...)
        record_bambi_entry_reasons: List[str] = Field(...) 
        record_bambi_departure_date: Optional[List[datetime]] 
        record_bambi_departure_reason: Optional[List[str]]
        record_justice_organization: str = Field(...,min_length=5)

        responsible_names: Optional[List[str]]
        responsible_identification: Optional[List[str]]
        responsible_contact: Optional[List[str]]
        