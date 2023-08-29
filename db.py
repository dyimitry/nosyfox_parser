import os

from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
import requests
load_dotenv()


Base = declarative_base()

connection = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('POSTGRES_USER'),
                              password=os.getenv('POSTGRES_PASSWORD'))
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

engine = create_engine('postgresql+psycopg2://postgres:example@localhost:5432/postgres', echo=True)
# session = Session(engine)
engine.connect()

cursor.close()
connection.close()


class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    volume = Column(Float)
    added_at = Column(String(20))
    strenght = Column(Integer)
    country = Column(String(200))


class Shop(Base):
    __tablename__ = 'Shop'
    id = Column(Integer, primary_key=True)
    adress = Column(String(200))


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))


Base.metadata.create_all(engine)

