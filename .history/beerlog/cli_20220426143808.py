import sys
from .config import settings


def main():
    #print("Hello from", settings.NAME)
    for attr in sys.argv[1:]:
        print("->", attr)
