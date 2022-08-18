from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import pokedex, typedex

app = FastAPI()
app.include_router(pokedex.router)
app.include_router(typedex.router)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/", tags = ["root"])
async def read_root() -> dict:
    return {"This is":"Fast React"}
