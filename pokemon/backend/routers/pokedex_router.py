from fastapi import APIRouter, Depends, HTTPException
from typing import List
from db.database import get_db
import db.classes as classes
import db.ops as ops

router = APIRouter(
    prefix = "/pokedex",
    tags=["pokedex"],
    responses={404: {"description": "Pokemon not found :("}},
)

@router.get("/", response_model=List[classes.Pokemon])
async def get_all_pokemon(db = Depends(get_db)):
    all= ops.get_all_pokemon(db)
    return all

@router.get("/{id}")
async def get_pokemon_id(id: int, db = Depends(get_db)):
    try:
        result = ops.get_pokemon_id(db, id)
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Pokemon with this ID was not found.",
        )
    return result

@router.get("/{name}")
async def get_pokemon_name(name: str, db = Depends(get_db)):
    try:
        result = ops.get_pokemon_name(db, name)
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Pokemon with this name was not found.",
        )
    return result