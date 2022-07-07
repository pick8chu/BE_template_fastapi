from asyncio.log import logger
# from tokenize import String
from fastapi.exceptions import HTTPException
import httpx
import asyncio
# import hmac
# import hashlib
# import constants
from config.base_config import logger

TEST_URL = "https://jsonplaceholder.typicode.com"

DEFAULT_HEADER = {
    'Accepts': 'application/json',
    'Content-type': 'application/json',
}

async def request(baseUrl:str, reqList:list, headers:dict = DEFAULT_HEADER) -> list:
    async with httpx.AsyncClient(headers=headers) as client:
        reqReadyList = []
        for req in reqList:
            uri = f"{baseUrl}{req['uri']}"
            data = req['data'] if 'params' in req.keys() else None
            reqReadyList.append(req['method'](client, uri, data))

        # gather is for multiple request
        resList = (await asyncio.gather(*reqReadyList))
        
        for i, res in enumerate(resList): 
            logger.info(f"{i}th :: client response :: status code :: {res.status_code}")
            logger.info(f"{i}th :: client response :: content :: {res.text}")
            
            if not httpx.codes.is_success(res.status_code):
                raise HTTPException(status_code=res.status_code, detail=f'reqNo: {i} : {res.text}')

        return list(map(lambda x: x.json(), resList))

# query param : params = { 'key': 'value' }
async def get(client, uri:str, data:dict) -> object:
    return await client.get(uri, params=data)

# request body : data = { 'key': 'value' }
async def post(client, uri:str, data:dict) -> object:
    return await client.post(uri, data=data)

# request body : data = { 'key': 'value' }
async def put(client, uri:str, data:dict) -> object:
    return await client.put(uri, data=data)

# request body : data = { 'key': 'value' }
async def delete(client, uri:str, data:dict) -> object:
    return await client.delete(uri, data=data)
