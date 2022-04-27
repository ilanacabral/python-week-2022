from typing import List, Optional
from sqlalchemy import delete
from sqlmodel import select
from sqlmodel import delete
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
        beer = Beer(name=name, style=style, flavor=flavor, image=image, cost=cost)
        session.add(beer)
        session.commit()
    return True

def get_beers_from_database() -> List[Beer]:
    with get_session() as session:
        sql = select(Beer)
        return list(session.exec(sql))

def get_beer_from_database(id:int) -> Beer:
    with get_session() as session:
        sql = select(Beer).where(Beer.id == id)
        #return session.exec(sql).first() # retorna Beer|None
        #return session.get(Beer,id) # retorna Beer|None
        return session.exec(sql).one() # se não encontra lança exceção     

def delete_beer_from_database(beer:Beer):
    with get_session() as session:
        session.delete(beer)
        session.commit()

def update_beer_from_database(beer:Beer):
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)