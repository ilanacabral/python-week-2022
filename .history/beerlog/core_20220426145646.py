from typing import List, Optional
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Beer

def add_beer_to_database(
     name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int
    ) -> bool:
    with get_session() as session:
        beer = Beer()
    return True