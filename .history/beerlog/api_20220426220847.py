from typing import List
from fastapi import FastAPI, Response # Usa protocolo ASGI 
from beerlog.core import get_beers_from_database, get_beer_from_database
from beerlog.database import get_session
from beerlog.serializers import BeerOut, BeerIn
from beerlog.models import Beer

api = FastAPI(title="Beerlog")

@api.get("/beers/", response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers

@api.get("/beers/{id}", response_model=List[BeerOut])
def get_beer(id:int):
    try:
    beer = get_beer_from_database(id=id)
    return beer

@api.post("/beers/",response_model=BeerOut)
def add_beer(beer_in:BeerIn):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer

