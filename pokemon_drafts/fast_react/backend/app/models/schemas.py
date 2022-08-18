import datetime
from typing import List
import pydantic

class Pokemon(pydantic.BaseModel):
    id = int
    name = str
    imgURL = str
    type1 = str
    type2 = str
    types = list
    
    class Config:
        orm_mode = True
        

class Type(pydantic.BaseModel):
    id = int
    name = str
    relations = list[list]
    
    class Config:
        orm_mode = True