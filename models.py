from sqlalchemy import Column, Integer, String
from connection import Base, schema

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': f'{schema}'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column(Integer, nullable=False, unique=True)
    designation = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)

