from typing import List
from fastapi import FastAPI, Response # Usa protocolo ASGI 
from beerlog.core import get_beers_from_database
from beerlog.models import Beer

api = FastAPI(title="Beerlog")

@api.get("/beers/", response_model=List[Beer])
def list_beers():
    beers = get_beers_from_database()
    return beers