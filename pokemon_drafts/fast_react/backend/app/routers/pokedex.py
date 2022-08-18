from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.pokemon import Pokemon
import models.schemas
import crud
import database

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix = "/pokemon",
    tags=["pokemon"],
    responses={404: {"description": "Pokemon not found"}},
)

@router.get("/", response_model=List[models.schemas.Pokemon])
async def get_all_pokemon(db = Depends(get_db)):
    all= crud.all_pokemon(db)
    return all

@router.get("/{id}")
async def get_one_pokemon(id: int, db = Depends(get_db)):
    try:
        crud.find_pokemon(db, id)
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Token does not exist",
        )
    result = crud.find_pokemon(db, id)
    return result

@router.post("/add")
async def add_pokemon(newPokemon: dict):
    allPokemon.append(newPokemon)
    return "{newPokemon} added."