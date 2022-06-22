from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    autonomus = Column(Boolean)
    make_id = Column(Integer, ForeignKey("makes.id"))
    engine_id = Column(Integer, ForeignKey("engines.id"))
    sold_id = Column(Integer, ForeignKey("solds.id"))
    
    # relationships
    sold = relationship("Sold", back_populates="cars")
    make = relationship("Make", back_populates="cars")
    engine = relationship("Engine", back_populates="cars")
    
class Sold(Base):
    __tablename__ = "solds"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    cars = relationship("Car", back_populates="sold")

class Make(Base):
    __tablename__ = "makes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    cars = relationship("Car", back_populates="make")

class Engine(Base):
    __tablename__ = "engines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    cars = relationship("Car", back_populates="engine")
