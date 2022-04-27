from typing import List
from fastapi import FastAPI, HTTPException, Response # Usa protocolo ASGI 
from beerlog.core import get_beers_from_database, get_beer_from_database, delete_beer
from beerlog.database import get_session
from beerlog.serializers import BeerOut, BeerIn
from beerlog.models import Beer
from sqlalchemy.exc import NoResultFound

api = FastAPI(title="Beerlog")

@api.get("/beers/", response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers

@api.get("/beers/{beer_id}", response_model=BeerOut)
def get_beer(beer_id:int):
    try:
        return get_beer_from_database(id=beer_id)       
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Beer not found")
    
@api.delete("/beers/{beer_id}", response_model=BeerOut)
def delete_beer(beer_id:int):
    try:
        beer = get_beer_from_database(id=beer_id)  
        delete_beer(beer)     
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Beer not found")

   
@api.post("/beers/",response_model=BeerOut)
def add_beer(beer_in:BeerIn):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer

