#Import database
from pkgutil import get_data
from model import Pokemon
import schema
from database import SessionLocal, engine
import model
from pull_api import pull_api

from fastapi import FastAPI #type:ignore #FastAPI class inherits from Starlette 
from fastapi.staticfiles import StaticFiles #type:ignore
from fastapi.templating import Jinja2Templates as Jinja #type:ignore

from fastapi import Depends, Request, Form #type:ignore
from sqlalchemy.orm import Session #type:ignore
from fastapi.responses import HTMLResponse #type:ignore

from starlette.responses import RedirectResponse, JSONResponse #type: ignore

#Create app instance
app = FastAPI()

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
async def find_all_pokemon(request: Request, db: Session = Depends(get_db)):
    all_pokemon = db.query(Pokemon).all()
    return templates.TemplateResponse("all.html", {"request": request, "all": all_pokemon})

@app.get("/pokemon/{id}", response_class=HTMLResponse)
def find_pokemon(request: Request, id: schema.Pokemon.id, db: Session = Depends(get_db)):
    this_pokemon = db.query(Pokemon).filter(Pokemon.id == id).first()
    print(this_pokemon)
    return templates.TemplateResponse("one_pokemon.html", {"request": request, "pokemon": this_pokemon})

@app.get("/add/", response_class=HTMLResponse)
async def serve_add(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("add.html")

@app.post("/add/")
async def create_pokemon(db: Session = Depends(get_db), name: schema.Pokemon.name = Form(...), url: schema.Pokemon.imgURL = Form(...), type: schema.Pokemon.type1 = Form(...)):
    new_pokemon = Pokemon(name=name, imgURL=url, type1=type)
    db.add(new_pokemon)
    db.commit()
    response = RedirectResponse("/", status_code=303)
    return response