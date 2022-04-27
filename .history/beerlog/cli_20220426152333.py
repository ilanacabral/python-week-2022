# import sys #importa info do sistema
#from .config import settings


# def main():
#print("Hello from", settings.NAME)
#    for attr in sys.argv[1:]:
#        print("->", attr)

import typer
from typing import Optional
from beerlog import database
from beerlog.core import add_beer_to_database
from beerlog.core import get_beers_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beer Management Application")

console = Console()  # adapta o consolo


@main.command("add")
def add(
    name: str,
    sytle: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...)
):
    """Adds a new beer to database"""
    if add_beer_to_database(name, sytle, flavor, image, cost):
        print("beer added to database")
    else:
        print("beer not added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "sytle", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(values)

    console.print(table)
