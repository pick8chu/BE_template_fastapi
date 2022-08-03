# from click import confirm
from re import template
import pytest
from config.base_config import logger
from fastapi.testclient import TestClient

from config.database import SQLALCHEMY_TEST_DATABASE_URI, get_db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
import src.template_api.template_service as template_service
from main import app

# from fastapi_utils.session import FastAPISessionMaker
# sessionmaker = FastAPISessionMaker(SQLALCHEMY_DATABASE_URI)

BASE_URI = "/people"

'''
creating database session
https://fastapi.tiangolo.com/advanced/testing-database/

Due to 2 different sessions, without commiting the data
it is not possible to check the data that is inserted.
'''
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URI, pool_pre_ping=True, echo=True)
TestingSessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# TODO: Need to make the sqeuence if you have one.
def test_create_and_get_person():
    # given
    createReq = getCreateReq()
    
    # when
    res = client.post(BASE_URI, json=createReq)

    # then 
    createdId = res.json()
    logger.info(f'createdId : {createdId}')
    confirmRes = client.get(f'{BASE_URI}/{createdId}')
    confirmModel = confirmRes.json()

    assert res.status_code == 200
    assert confirmRes.status_code == 200
    assert createReq["name"] == confirmModel["name"]

# def test_get_person():
#     # given
#     createReq = getCreateReq()
#     with sessionmaker.context_session() as db:
#         template_service.createPerson(createReq, db)
    
#     # when
#     res = client.post(f'{BASE_URI}', json=createReq)


def getCreateReq():
    return {
        "name": "John Ethan Doe",
        "job": "keyboard warrior",
        "age": 33
    }
