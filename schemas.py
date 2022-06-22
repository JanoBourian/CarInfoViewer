from pydantic import BaseModel, validator, Field
from typing import Optional, List


## Engine
class Engine(BaseModel):
    name: str

class DisplayEngine(Engine):
    name: str
    
    class Config:
        orm_mode = True

## Make
class Make(BaseModel):
    name: str

class DisplayMake(Make):
    name: str
    
    class Config:
        orm_mode = True

## Sold
class Sold(BaseModel):
    name: str

class DisplaySold(Sold):
    name: str
    
    class Config:
        orm_mode = True

## Car
class Car(BaseModel):
    model: str
    year: int = Field(..., ge = 1970, lt = 2022)
    price: float
    autonomus: bool
    make_id: int
    engine_id: int
    sold_id: int

class DisplayCar(Car):
    model: str
    year: int
    price: float
    autonomus: bool
    make: DisplayMake
    engine: DisplayEngine
    sold: DisplaySold
    
    class Config:
        orm_mode = True
    