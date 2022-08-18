from logging.config import fileConfig
from alembic import context

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from database import Base
import models.pokemon, models.type

USER = "root"
PASSWORD = "Burget136!!"
HOST = "pokemondb.c1bl7gpkpozr.us-east-1.rds.amazonaws.com"
DATABASE = "pokemondb"

target_metadata =[Base.metadata]


def run_migrations_offline() -> None:
    url = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_server_default = True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    url = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    connectable = engine_from_config(
        {"sqlalchemy.url": url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
