from sqlalchemy import create_engine    #type: ignore
from sqlalchemy.ext.declarative import declarative_base #type: ignore
from sqlalchemy.orm import sessionmaker #type: ignore

DATABASE_URL = "mysql+mysqlconnector://root:Burget136!!@pokemondb.c1bl7gpkpozr.us-east-1.rds.amazonaws.com/pokemondb"
engine = create_engine(DATABASE_URL, pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

