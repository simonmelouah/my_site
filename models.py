from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(50))
    password = Column(String(150))

class Technology(Base):
    __tablename__ = 'technology'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image = Column(String(150))

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key = True)
    timestamp = Column(DateTime)
    technology_id = Column(Integer)
    category_id = Column(Integer)
    title = Column(String(50))
    description = Column(String(1000))
    url = Column(String(150))
    youtube = Column(String(150))
    hovers = Column(Integer)
    clicks = Column(Integer)

class WebPage(Base):
    __tablename__ = 'web_page'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    name = Column(String(50))

class PageTracking(Base):
    __tablename__ = 'page_tracking'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    web_page_id = Column(Integer)
    time_spent = Column(Float)
