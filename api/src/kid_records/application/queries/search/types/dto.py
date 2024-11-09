from pydantic import BaseModel, Field
from datetime import datetime  
from typing import List, Optional

class Search_kid_dto(BaseModel):
    page:Optional[int] = Field(ge=0,default=0)
    per_page:Optional[int] = Field(ge=0,default=10)
    search: str = Field(..., min_length=3)
    

        

