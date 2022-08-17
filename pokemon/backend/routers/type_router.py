from fastapi import APIRouter, Depends, HTTPException
from typing import List
from db.database import get_db
import db.classes as classes
import db.ops as ops

router = APIRouter(
    prefix = "/type",
    tags=["type"],
    responses={404: {"description": "Type not found"}},
)

@router.get("/", response_model=List[classes.Type])
async def get_all_type(db = Depends(get_db)):
    all= ops.get_all_type(db)
    return all

@router.get("/{name}")
async def get_type_name(name: str, db = Depends(get_db)):
    try:
        result = ops.get_pokemon_id(db, name)
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Type with this name was not found.",
        )
    return result