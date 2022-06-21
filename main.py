from fastapi import FastAPI
from config import config
from routers import car
from database import engine
from models import Base 

app = FastAPI(**config)

# Router
app.include_router(car.router)

# Create table
Base.metadata.create_all(engine)

