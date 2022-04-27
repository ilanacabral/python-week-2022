from fastapi import FastAPI # Usa protocolo ASGI 
from beerlog.core import get_beers_from_database
api = FastAPI(title="Beerlog")

def list_beers():
    beers = get_beers_from_database()
    return beers
