#Fast API Imports
from fastapi import FastAPI, Depends, Request, Form #type:ignore
from fastapi.staticfiles import StaticFiles #type:ignore
from fastapi.templating import Jinja2Templates as Jinja #type:ignore
from fastapi.responses import HTMLResponse #type:ignore
from starlette.responses import RedirectResponse, JSONResponse #type: ignore
from fastapi.middleware.cors import CORSMiddleware

#DB Imports
from sqlalchemy.orm import Session #type:ignore
from pkgutil import get_data
from model import Pokemon, Types
import schema, model
from database import SessionLocal, engine
from pull_api import pull_api

#Other Imports
from pydantic import AnyHttpUrl
from typing import List, Optional

#Create app instance
app = FastAPI()

#Set CORS
BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000","http://localhost:8000"]
BACKEND_CORS_ORIGIN_REGEX: Optional[str] = "https.*\.(netlify.app|herokuapp.com)"
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
    allow_origin_regex = BACKEND_CORS_ORIGIN_REGEX,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


#Create tables and bind database engine
model.Base.metadata.create_all(bind=engine)
pull_api()
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Add static files to application
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja(directory="templates")


#Path Operations
@app.get("/")
async def read_root():
    return {"Home Page"}

@app.get("/pokemon", response_class=HTMLResponse)
async def get_all_pokemon(request: Request, db: Session = Depends(get_db)):
    all_pokemon = db.query(Pokemon).all()
    return templates.TemplateResponse("all_pokemon.html", {"request": request, "all": all_pokemon})

@app.get("/pokemon/{id}", response_class=HTMLResponse)
async def get_one_pokemon(request: Request, id: schema.Pokemon.id, db: Session = Depends(get_db)):
    this_pokemon = db.query(Pokemon).filter(Pokemon.id == id).first()
    return templates.TemplateResponse("one_pokemon.html", {"request": request, "pokemon": this_pokemon})

@app.get("/type", response_class=HTMLResponse)
async def get_all_types(request: Request, db: Session = Depends(get_db)):
    all_types = db.query(Types).all()
    
    return templates.TemplateResponse("all_types.html", {"request": request, "all": all_types})

@app.get("/type/{id}", response_class = HTMLResponse)
async def get_one_type(request: Request, id: schema.Types.id, db: Session = Depends(get_db)):
    this_type = db.query(Types).filter(Types.id == id).first()
    return templates.TemplateResponse("one_type.html", {"request": request, "type": this_type})