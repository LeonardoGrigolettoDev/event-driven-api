from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class UserDB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class DeviceDB(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
