from sqlmodel import create_engine

engine = create_engine(settings.database.url)