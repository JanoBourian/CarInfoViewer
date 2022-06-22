from fastapi import APIRouter, Response, status, HTTPException
from schemas import Car, DisplayCar

router = APIRouter(tags = ["car"], prefix ="/cars")

## Car endpoints

@router.get("/", tags=["index"])
async def index():
    return {"message": "Hello man, good evening"}