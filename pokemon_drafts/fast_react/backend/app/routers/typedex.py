from fastapi import APIRouter, Depends, HTTPException
import models.type

router = APIRouter(
    prefix = "/type",
    tags=["items"],
    responses={404: {"description": "Type not found"}},
)

@router.get("/")
async def get_all_types():
    return allTypes

@router.get("/{name}")
async def get_one_type(name: str):
    found = [type for type in allTypes if type["name"] == name.lower()]
    if found:
        return found
    else:
        return "Does not exist"

@router.post("/add")
async def add_add(newType: dict):
    allTypes.append(newType)
    return "{newType} added."