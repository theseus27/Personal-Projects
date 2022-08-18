from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

from enum import auto
from sqlalchemy.schema import Column    #type: ignore
from sqlalchemy.types import String, Integer, Text  #type: ignore
from sqlalchemy.ext.hybrid import hybrid_property as hybrid
import json
import requests

class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(50), nullable = False)
    imgURL = Column(String(999))
    type1 = Column(String(20))
    type2 = Column(String(20))
    
    #Make a hybrid property to return only types that are not null
    @hybrid
    def types(self):
        type_list = [self.type1, self.type2]
        return [type for type in type_list if type != ""]
    
    @hybrid
    def to_json(self):
        values = {
            "id": self.id,
            "name": self.name,
            "imgURL": self.imgURL,
            "type1": self.type1,
            "type2": self.type2
        }
        return json.dumps(values)



"""
allPokemon = [
    {
        "id": "1",
        "num": "1",
        "name": "Bulbasaur",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
    },
    {
        "id": "2",
        "num": "4",
        "name": "Charmander",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
    },
    {
        "id": "3",
        "num": "7",
       
        "name": "Squirtle",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"
    },
    {
        "id": "4",
        "num": "25",
        "name": "Pikachu",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png" 
    }
]
"""

""" Post request format
{"id":"5","num":"393","name":"piplup","img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/393.png"}
"""