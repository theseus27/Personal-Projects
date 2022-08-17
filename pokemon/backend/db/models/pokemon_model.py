from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from enum import auto
from sqlalchemy.schema import Column    #type: ignore
from sqlalchemy.types import String, Integer, Text  #type: ignore
from sqlalchemy.ext.hybrid import hybrid_property as hybrid
import json
import classes

class Pokemon(Base):
    __tablename__ = "pokedex"
    
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(), nullable = False)
    generation = Column(Integer, nullable = False)
    imgURL = Column(String())
        
    types_data = Column(String())
    moves_data = Column(String())
    abilities_data = Column(String())
    base_stats_data = Column(String())
    
    @hybrid
    def types(self):
        type_list = []
        for type in self.types:
            type_list.append(type.get("type").get("name"))
            
        #assert (len(type_list) > 0)
        return type_list
    
    @hybrid
    def to_json(self) -> str:
        values = {
            "id": self.id,
            "name": self.name,
            "generation": self.generation,
            "imgURL": self.imgURL,
            "types": self.types()
        }
        return json.dumps(values)