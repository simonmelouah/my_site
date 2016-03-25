from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

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
    image = Column(String(150))

class Categories(Base):
    __tablename__ = 'Categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Projects(Base):
    __tablename__ = 'Projects'
    id = Column(Integer, primary_key = True)
    timestamp = Column(DATETIME)
    lookup_technologies = Column(Integer)
    lookup_categories = Column(Integer)
    title = Column(String(50))
    description = Column(String(500))
    url = Column(String(150))
    youtube = Column(String(150))


