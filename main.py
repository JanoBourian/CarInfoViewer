from fastapi import FastAPI
from config import config
from routers import car
from routers.engine import router as engine_router
from database import engine
from models import Base 

app = FastAPI(**config)

# Router
app.include_router(car.router)
app.include_router(engine_router)

# Create table
Base.metadata.create_all(engine)

