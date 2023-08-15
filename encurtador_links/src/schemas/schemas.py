from pydantic import BaseModel
from typing import Optional, List

class Url(BaseModel):
    url: str
    
    class Config:
        from_attributes = True