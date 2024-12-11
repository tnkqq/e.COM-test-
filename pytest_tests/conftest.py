import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from .utils import generate_form_by_pattern
from tinydb import TinyDB


@pytest_asyncio.fixture
def database():

    db = TinyDB("forms.json")

    return db

@pytest.fixture(scope="module")
def app():
    from src.app import app

    return app


@pytest_asyncio.fixture
async def client(app: FastAPI, database):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest_asyncio.fixture
async def forms(database):
    '''
    -> (pattern, form)
    '''

    db = database
    patterns = db.all()
    pattern = patterns[-1]

    form=generate_form_by_pattern(pattern)

    return (pattern.get('name'), form)
