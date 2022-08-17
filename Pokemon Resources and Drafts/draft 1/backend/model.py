from enum import auto
from sqlalchemy.schema import Column    #type: ignore
from sqlalchemy.types import String, Integer, Text  #type: ignore
from database import Base
from sqlalchemy.ext.hybrid import hybrid_property as hybrid
import json, requests

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

class Types(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(50), nullable = False)
    
    @hybrid
    def relations(self):
        response = requests.get(f"https://pokeapi.co/api/v2/type/{self.id}")
        data = json.loads(response.content)
        
        relation_keys = ["double_damage_from", "double_damage_to", "half_damage_from", "half_damage_to", "no_damage_from", "half_damage_to"]
        rk_short = ["2f", "2t", ".5f", ".5t", "0f", "0t"]
        relation_data = []
        for i in relation_keys:
                relation_data.append(data.get("damage_relations").get(i))

        relations = {}
        for index, data in enumerate(relation_data):
            list= [j.get("name") for j in data]
            if list == []:
                list = ["none"]
            relations[rk_short[index]] = list
        
        return relations