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

class ProjectTracking(Base):
    __tablename__ = 'project_tracking'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    project_id = Column(Integer)
    interaction_type = Column(String(50))

class WebPage(Base):
    __tablename__ = 'web_page'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    name = Column(String(50))

class WebPageTracking(Base):
    __tablename__ = 'web_page_tracking'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    web_page_id = Column(Integer)
    time_spent = Column(Float)

class MouseRecording(Base):
    __tablename__ = 'mouse_recording'
    id = Column(Integer, primary_key=True)
    session_id = Column(String(20))
    timestamp = Column(DateTime)
    event_type = Column(String(10))
    window_width = Column(Float)
    window_height = Column(Float)
    x_position = Column(Float)
    y_position = Column(Float)
