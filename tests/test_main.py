# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)


# async def test():
#     req = {"method":webClient.get, "uri":'/posts'}
#     res = await webClient.request(baseUrl=webClient.BASE_URL, reqList=[req])
#     logger.info(res)
#     assert res != None

# add short list test cases

# def test_addShortList():
#     response = client.post("/short-links", json={"url":"https://www.youtube.com/"})
#     assert response.status_code == 200

# def test_invalidUrl():
#     response = client.post("/short-links", json={"url":"abcdefu"})
#     assert response.status_code == 400

# def test_leftSpace():
#     response = client.post("/short-links", json={"url":"    https://www.youtube.com/"})
#     assert response.status_code == 200

# def test_rightSpace():
#     response = client.post("/short-links", json={"url":"https://www.youtube.com/             "})
#     assert response.status_code == 200

# # get short list test cases

# def test_getShortList():
#     shortId = "test1"
#     response = client.get(f"/short-links/{shortId}")
#     assert response.status_code == 200
#     assert response.json() == {
#         'shortId': 'test1', 
#         'url': 'https://www.youtube.com/', 
#         'createAt': '2022-06-04T15:24:53.758737+09:00'
#     }

# def test_shortIdNotExist():
#     shortId = "====="
#     response = client.get(f"/short-links/{shortId}")
#     assert response.status_code == 404

# # redirect test cases

# # # redirection is difficult to assert in test environment:
# # # one can use curl / swagger
# # def test_redirect():
# #     shortId = "test1"
# #     response = client.get(f"/{shortId}")
# #     print(response.json())
    
# #     assert response.status_code == 302

# def test_redirectShortIdNotExist():
#     shortId = "====="
#     response = client.get(f"/{shortId}")
#     assert response.status_code == 404