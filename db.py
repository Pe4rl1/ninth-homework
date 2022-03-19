from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

user = 'postgres'
passwd = '21012006'
host = 'localhost'
port = '5432'

# Postgres
 url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'

# SQLite
 #url = 'sqlite:///local.db'

engine = create_engine(url, echo=False)
Base = declarative_base()


def execute(*args, **kwargs):
    with engine.connect() as conn:
        return conn.execute(*args, **kwargs)
