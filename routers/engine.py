from fastapi import APIRouter, Response, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.params import Depends
from typing import List
from database import get_db
import models 
import schemas

router = APIRouter(prefix="/engine", tags=["engine"])

@router.get("/", response_model = List[schemas.DisplayEngine])
async def get_all_engines(response:Response, db:Session = Depends(get_db)):
    response.status_code = status.HTTP_200_OK
    return get_engines(db)

@router.post("/", response_model = schemas.DisplayEngine)
async def create_engine(response:Response, request:schemas.Engine, db:Session = Depends(get_db)):
    if get_engine_by_name(db, name=request.name):
        raise HTTPException( status_code = status.HTTP_404_NOT_FOUND, detail = f"Engine {request.name} already exists" )
    new_engine = create_engine(request, db)
    response.status_code = status.HTTP_201_CREATED
    return new_engine

### CRUD Operations

def get_engines(db:Session):
    return db.query(models.Engine).all()

def get_engine_by_name(db:Session, name:str):
    return db.query(models.Engine).filter(models.Engine.name == name).first()

def create_engine(engine:schemas.Engine, db:Session):
    new_engine = models.Engine(
        **engine.dict()
    )
    db.add(new_engine)
    db.commit()
    db.refresh(new_engine)
    return new_engine
    
def update_engine():
    return True