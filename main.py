from fastapi import FastAPI, Depends, Request, Response, Query, Body
from src.template_api import template_routes
from fastapi.middleware.cors import CORSMiddleware
import hmac
import hashlib
from config.base_config import logger
# this will start the batch
# import schedule 

app = FastAPI()
app.include_router(template_routes.router)

# to log all the request/response

# @app.middleware("http")
# async def log_request(request, call_next):
#     logger.info(f'{request.method} {request.url}')
#     response = await call_next(request)
#     logger.info(f'Status code: {response.status_code}')
#     body = b""
#     async for chunk in response.body_iterator:
#         body += chunk
    
#     # TODO: list body cannot be convert to hmac -> it won't work as an auth.
#     body = body    
#     #'bytes' object has no attribute 'encode'
#     signature = hmac.new(key.encode('utf-8'), body, hashlib.sha256).hexdigest()
    
#     return Response(
#         content={"data":body, 'signature':signature},
#         status_code=response.status_code,
#         headers=dict(response.headers),
#         media_type=response.media_type
#     )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["http://localhost:8080", "Access-Control-Allow-Origin"],
)
