from csv import list_dialects
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List, Optional

import src.template_api.template_model as template_model
from . import template_service
from config.database import get_db

# BASE_URI = "/people"
router = APIRouter(prefix="/people")

''', response_model=schemas.Task, operation_id="create_task"'''
@router.post("", operation_id="create a person's info")
def createPerson(createReq: template_model.CreateReq, db: Session = Depends(get_db)):
    return template_service.createPerson(createReq, db)

@router.get("", response_model=List[template_model.SearchRes], operation_id="get people info")
def getPeople(db: Session = Depends(get_db)):
    return template_service.getPeople(db)

@router.put("/{id}", operation_id="edit a person's info")
def editPerson(id: int, editReq: template_model.EditReq, db: Session = Depends(get_db)):
    return template_service.editPerson(id, editReq, db)

@router.get("/{id}", response_model=template_model.SearchRes, operation_id="get a person's info")
def getPerson(id: int, db: Session = Depends(get_db)):
    return template_service.getPerson(id, db)

@router.delete("/{id}", operation_id="delete a person's info")
def removePerson(id: int, db: Session = Depends(get_db)):
    return template_service.removePerson(id, db)





#  quote Cache / Update frequency: Every 60 seconds.
# @router.get("/people")
# async def getQuotes(symbols:str='BTC,ETH', currencys:str='KRW'):
#     return await service.getQuotes(symbols, currencys)

# @router.get("/quote-history/{symbols}")
# async def getQuoteHistory(dateFrom:str, dateTo:str, symbols:str='BTC,USDT', currencys:str='USD', db: Session = Depends(get_db)):
#     return await service.getQuoteHistory(dateFrom, dateTo, symbols, currencys, db)
     
# @router.post("/quotes/{symbols}")
# async def addQuotes(symbols: str='BTC,USDT,ETH,XRP,ATOM', currencys: str='USD,KRW', db: Session = Depends(get_db)):
#     await service.addQuotes(symbols, currencys, db)
     
# @router.post("/quotes/list")
# async def addQuoteList(db: Session = Depends(get_db)):
#     await service.addQuoteList(db)
     
