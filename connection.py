from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "postgres"
# schema = "public"
schema = "TestSchema"
SQL_BASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(SQL_BASE_URL)

# engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

# engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
