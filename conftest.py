from os import sched_param
from tempfile import tempdir
import pytest
from unittest.mock import patch
from sqlmodel import create_engine
from beerlog import models

@pytest.fixture(autouse=True,scope="function")
def each_uses_separete_database(request):
    tmpdir = request.getfixturevalue("tmpdir")
    