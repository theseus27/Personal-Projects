from enum import auto
from sqlalchemy.schema import Column    #type: ignore
from sqlalchemy.types import String, Integer, Text  #type: ignore
from database import Base
from sqlalchemy.ext.hybrid import hybrid_property as hybrid

class Pokemon(Base):
    __tablename__ = "Pokemon"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50), nullable = False)
    imgURL = Column(String(999))
    type1 = Column(String(20))
    type2 = Column(String(20))
    
    #Make a hybrid property to return only types that are not null
    @hybrid
    def types(self):
        type_list = [self.type1, self.type2]
        return [type for type in type_list if type != ""]