from datetime import date
from pydantic import BaseModel  #type: ignore

class Pokemon(BaseModel):
    id = int
    name = str
    imgURL = str
    type1 = str
    type2 = str
    
    class Config:
        orm_mode = True
