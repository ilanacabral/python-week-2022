from pydantic import BaseModel
from datetime import datetime

class BeerOut(BaseModel):
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime

class BeerIn(BaseModel):
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime