from typing import Optional
from sqlmodel import Field, SQLModel, values
from sqlmodel import select
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True,default=None)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int=0
    date : datetime = Field(default_factory=datetime.now)

    @validator("flavor","image","cost")
    def validate_ratings(cls,v, field):
        if v < 1 or v > 10 :
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v   

   

try :
    brewdog = Beer(name="Bewdog",style="NEIPA", flavor=60, image=8, cost=8)
except RuntimeError:
    print("Zika demais!")

