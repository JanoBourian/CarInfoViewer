from pydantic import BaseModel, validator, Field
from typing import Optional, List

class Car(BaseModel):
    id: int
    make: str 
    model: str
    year: int = Field(..., ge = 1970, lt = 2022)
    price: float
    engine: Optional[str] = "V4"
    autonomus: bool
    sold: List[str]
    
    