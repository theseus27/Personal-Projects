from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from enum import auto
from sqlalchemy.schema import Column    #type: ignore
from sqlalchemy.types import String, Integer, Text  #type: ignore
from database import Base
from sqlalchemy.ext.hybrid import hybrid_property as hybrid
import json
import classes

class Move(Base):
    __tablename__ = "moves"
    
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(), nullable = False)
    accuracy = Column(Integer)
    damage_class = Column(String())
    effect_chance = Column(Integer)
    effect_changes = Column(String())
    description =  Column(String()) #Takes effect chance as a variable
    power = Column(Integer)
    pp = Column(Integer)
    priority = Column(Integer)
    stat_changes = Column(String())
    type = Column(String())
    
    pokemon_data = Column(String())
        