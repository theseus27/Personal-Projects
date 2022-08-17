from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import pokedex_router, type_router

app = FastAPI()
app.include_router(pokedex_router.router)
app.include_router(type_router.router)

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
async def read_root() -> str:
    return "Pokemon Home Screen"