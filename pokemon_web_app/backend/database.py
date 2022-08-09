from sqlalchemy import create_engine    #type: ignore
from sqlalchemy.ext.declarative import declarative_base #type: ignore
from sqlalchemy.orm import sessionmaker #type: ignore

DATABASE_URL = "mysql+mysqlconnector://pokemonappuser@localhost:3306/serversiderendering"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()