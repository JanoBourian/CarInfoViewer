from fastapi import FastAPI, APIRouter

router = APIRouter(tags = ["car"], prefix ="/cars")

## Car endpoints

@router.get("/", tags=["index"])
async def index():
    return {"message": "Hello man, good evening"}