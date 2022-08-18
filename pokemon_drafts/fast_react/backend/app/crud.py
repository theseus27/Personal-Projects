from sqlalchemy import select
from sqlalchemy.orm import Session

from models.pokemon import Pokemon
from models.type import Type
import json

def find_pokemon(db: Session, pokemon_id: int):
    pokemon_query = select(Pokemon).where(Pokemon.id == pokemon_id)
    pokemon = db.execute(pokemon_query).first()[0]
    
    values = {
        "id": pokemon.id,
        "name": pokemon.name,
        "imgURL": pokemon.imgURL,
        "type1": pokemon.type1,
        "type2": pokemon.type2
    }
    
    return json.dumps(values)

def all_pokemon(db: Session):
    query = select(Pokemon)
    pokemon = db.execute(query).all()
    return pokemon