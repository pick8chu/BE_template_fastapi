from config.base_config import logger
from fastapi.testclient import TestClient
import config.client as webClient
from main import app

client = TestClient(app)

# test will be only conducted to funtions that have "test_" as prefix.

# GET test
async def test_client_get():
    pathParam = "1"
    req = {"method":webClient.get, "uri":f'/posts/{pathParam}'}
    resList = await testWebClient(reqList=[req])

    printResult(resList)

    assert len(resList) == 1

    
# GET test
'''
    HTTPX send multiple request simultaneously, which makes it very efficient.
    req1 - res1 
     req2 - res2
      req3 - req3 -> return responseList
'''
async def test_client_get_multi():
    pathParamList = ["1","2","3"]
    reqList = [{"method":webClient.get, "uri":f'/posts/{pathParam}'} for pathParam in pathParamList]
    resList = await testWebClient(reqList=reqList)

    printResult(resList)

    assert len(resList) == 3


# POST test - response.status == 201
async def test_client_post():
    reqParam = {
        "title": "TEST",
        "body": "BAR",
        "userId": 1,
    }
    req = {"method":webClient.post, "uri":'/posts', "data": reqParam}
    resList = await testWebClient(reqList=[req])

    printResult(resList)

    assert len(resList) == 1



# PUT test
async def test_client_put():
    pathParam = "1"
    reqParam = {
        'id': 1,
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    req = {"method":webClient.put, "uri":f'/posts/{pathParam}', "data": reqParam}
    resList = await testWebClient(reqList=[req])

    printResult(resList)

    assert len(resList) == 1

    
# DELETE test
async def test_client_delete():
    pathParam = "1"
    req = {"method":webClient.put, "uri":f'/posts/{pathParam}'}
    resList = await testWebClient(reqList=[req])

    printResult(resList)

    assert len(resList) == 1

def printResult(resList):
    for res in resList:
        logger.info(res)

async def testWebClient(reqList:list):
    return await webClient.request(baseUrl=webClient.TEST_URL, reqList=reqList)