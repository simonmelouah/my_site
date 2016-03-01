#This python file builds all sql tables using sqlalchemy
# import pyodbc;
from sqlalchemy import *;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base;
import urllib;
from datetime import datetime, timedelta;
from dateutil import tz;

#Proper method of getting accurate local time
from_zone = tz.tzutc()
to_zone = tz.tzlocal()
utc = datetime.utcnow()
utc = utc.replace(tzinfo = from_zone)
central = utc.astimezone(to_zone)
offset = int(central.strftime("%z")) 
Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key = True)
    username = Column(String(50))
    password = Column(String(150))

#Classes for sql tables
class Projects(Base):
    __tablename__ = 'Projects'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    url = Column(String(150))

