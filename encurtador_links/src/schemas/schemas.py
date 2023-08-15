from pydantic import BaseModel
from typing import Optional, List

class Url(BaseModel):
    url: str
    url_encurtada: str
    
    class Config:
        from_attributes = True