from ast import Delete
from typing import List
from fastapi import FastAPI, HTTPException, Response,status # Usa protocolo ASGI 
from beerlog.core import get_beers_from_database, get_beer_from_database, delete_beer_from_database,update_beer_from_database
from beerlog.database import get_session
from beerlog.serializers import BeerOut, BeerIn
from beerlog.models import Beer
from sqlalchemy.exc import NoResultFound
from fastapi.encoders import jsonable_encoder

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
    
@api.delete("/beers/{beer_id}",status_code=status.HTTP_200_OK)
def delete_beer(beer_id:int):
    try:
        beer = get_beer_from_database(id=beer_id)      
        delete_beer_from_database(beer)  
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Beer not found")

@api.patch("/beers/{beer_id}",response_model=BeerOut)
def update_partial_beer(beer_id:int,beer:Beer):
    try:
        stored_beer_data  = get_beer_from_database(id=beer_id)  
        stored_beer_model = Beer(**jsonable_encoder(stored_beer_data))
        update_data = beer.dict(exclude_unset=True)
        updated_beer = stored_beer_model.copy(update=update_data)        
        update_beer_from_database(updated_beer)
        return updated_beer
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

