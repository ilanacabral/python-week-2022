# import sys #importa info do sistema
#from .config import settings


# def main():
#print("Hello from", settings.NAME)
#    for attr in sys.argv[1:]:
#        print("->", attr)

import typer
from beerlog import database
from beerlog.core import add_beer_to_database

main = typer.Typer(help="Beer Management Application")

@main.command("add")
def add(
        name :str, 
        sytle:str,
        flavor : int =typer.Option(...),
        image: int = typer.Option(...),
        cost: int = typer.Option(...)
    ):
    """Adds a new beer to database"""
    if add_beer_to_database(name,sytle,flavor,image,cost):
            print("beer added to database")
    else:
            print("beer not added to database")

@main.command("list")
def list_beers(style:str):
    """Lists beers in database"""
    print(style)


