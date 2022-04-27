# import sys #importa info do sistema
#from .config import settings


# def main():
#print("Hello from", settings.NAME)
#    for attr in sys.argv[1:]:
#        print("->", attr)

import typer
main = typer.Typer(help="Beer Management Application")

def add(name :str, sytle:str):
    print(name,sytle)

