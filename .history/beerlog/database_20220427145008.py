import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel import create_engine, Session
from beerlog.config import settings
from beerlog import models

warnings.filterwarnings("ignore",category=SAWarning)
SelectOfScalar

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)