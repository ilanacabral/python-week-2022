from urllib.error import HTTPError
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

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HttPValidationError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate",always=True)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values["flavor"],
                values["image"],
                values["cost"]
            ]
        )
        return int(rate)