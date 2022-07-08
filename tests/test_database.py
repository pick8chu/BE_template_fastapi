import pytest
from config.base_config import logger
from fastapi.testclient import TestClient

from config.database import SQLALCHEMY_DATABASE_URI, get_db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
import src.template_api.template_service as template_service
from main import app

# from fastapi_utils.session import FastAPISessionMaker
# sessionmaker = FastAPISessionMaker(SQLALCHEMY_DATABASE_URI)

BASE_URI = "/people"

client = TestClient(app)

'''
creating database session
https://fastapi.tiangolo.com/advanced/testing-database/
'''
engine = create_engine(SQLALCHEMY_DATABASE_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        print("here")
        db.rollback()
        db.close()

# this is for routes parameter
app.dependency_overrides[get_db] = override_get_db

'''
till here
'''

# this is for service parameter
# TODO: rollback is not working properly
@pytest.fixture
def db_session():
    connection = create_engine(SQLALCHEMY_DATABASE_URI)
    sessionTest = sessionmaker(autocommit=False, autoflush=True, bind=connection)
    db = sessionTest()
    try:
        yield db
    finally:
        print("here2")
        db.rollback()
        db.close()

# TODO: need to combine sessions of client and service.... how?
def test_create_person(db_session):
    # given
    createReq = getCreateReq()
    
    # when
    res = client.post(BASE_URI, json=createReq)

    # then 
    createdId = res.json()
    resModel = template_service.getPerson(createdId, db_session)
    logger.info(resModel)

    assert res.status_code == 200
    assert createReq["name"] == resModel.name

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
