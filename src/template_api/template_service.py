import config.client as client
import re
from sqlalchemy.orm import Session
# from src.template_api.dvo import Quote
from sqlalchemy import and_, or_, not_
from src.template_api.template_dvo import Person
import src.template_api.template_model as template_model
from config.base_config import logger

# USD = "USD"
# KRW = "KRW"
# QUOTES_URI = "/v2/cryptocurrency/quotes/latest"
# QUOTE_LIST_URI = "/v1/cryptocurrency/listings/latest"

def createPerson(createReq: template_model.CreateReq, db: Session) -> int:
    model = Person(**createReq.dict())
    db.add(model)
    db.commit() 
    return model.id 

def getPeople(db: Session) -> list[Person]:
    return db.query(Person).filter(
        # and_(
        #     Quote.symbol.in_(symbols.split(',')),
        #     Quote.currency.in_(currencys.split('m')),
        #     Quote.last_updated.between(dateFrom, dateTo)
        # )
    ).all()
    
def editPerson(id: int, editPerson: template_model.EditReq, db: Session) -> int:
    # person = db.query(Person).filter(Person.id == id).one_or_none()
    db.query(Person).filter(Person.id == id).update(editPerson.dict())
    db.commit() 
    return 1

def getPerson(id: int, db: Session) -> Person:
    return db.query(Person).filter(Person.id == id).one_or_none()
    
def removePerson(id: int, db: Session) -> int:
    person = db.query(Person).filter(Person.id == id).one_or_none()
    db.delete(person)
    db.commit()
    return 1
    


# async def addQuotes(symbols:str, currencys:str, db: Session):
#     # multiple currency not supported with basic plan
#     [symbols, currencys] = spaceRemover(symbols, currencys)

#     currencyList = currencys.split(',')
#     reqList = [{"method":client.get, "uri":QUOTES_URI, "params":paramBuilder(symbols, currency)} for currency in currencyList]
    
#     resList = await client.request(reqList)
    
#     for res in resList:
#         for symbol in res:
#             for quote in res[symbol]:
#                 db.add(Quote.convertFromDict(quote))
                
#     db.commit() 

# async def addQuoteList(db: Session):
#     currencys = [KRW, USD]
#     reqList = [{"method":client.get, "uri":QUOTE_LIST_URI, "params":{"start":1 + (idx*200), "limit":200, "convert":currency}} for idx in range(3) for currency in currencys]
        
#     resList = await client.request(reqList)
    
#     for res in resList:
#         for quote in res:
#             db.add(Quote.convertFromDict(quote))
                
#     db.commit() 

# async def getQuotes(symbols:str, currencys:str):
#     [symbols, currencys] = spaceRemover(symbols, currencys)

#     resList = await client.request([{"method":client.get, "uri":QUOTES_URI, "params":paramBuilder(symbols, currencys)}])
    
#     quoteList = []
#     for res in resList:
#         for symbol in res:
#             for quote in res[symbol]:
#                 quoteList.append(Quote.convertFromDict(quote))
#     return quoteList

# async def getQuoteHistory(dateFrom:str, dateTo:str, symbols:str, currencys:str, db: Session):
#     [symbols, currencys] = spaceRemover(symbols, currencys)
#     res = db.query(Quote).filter(
#         and_(
#             Quote.symbol.in_(symbols.split(',')),
#             Quote.currency.in_(currencys.split('m')),
#             Quote.last_updated.between(dateFrom, dateTo)
#         )
#     ).all()
#     return res

# def paramBuilder(symbol:str, currency:str):
#         'convert':currency 
#     }

# def spaceRemover(*strList:str):
#     return [re.sub(r"\s", "", str) for str in strList] 