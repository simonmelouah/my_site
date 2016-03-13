#This python file builds all sql tables using sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib
from datetime import datetime, timedelta


Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key = True)
    username = Column(String(50))
    password = Column(String(150))

class Technologies(Base):
    __tablename__ = 'Technologies'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    value = Column(String(50))
    image = Column(String(150))

class Projects(Base):
    __tablename__ = 'Projects'
    id = Column(Integer, primary_key = True)
    lookup_technologies = Column(Integer)
    title = Column(String(50))
    description = Column(String(500))
    url = Column(String(150))


