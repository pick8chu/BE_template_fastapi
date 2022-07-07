from datetime import datetime
from pydantic import BaseModel
from src.template_api.template_dvo import Person

class CreateReq(BaseModel):
    name: str
    job: str | None = None #nullable
    age: int | None = None

class EditReq(BaseModel):
    name: str
    job: str | None = None #nullable
    age: int | None = None

class SearchRes(BaseModel):
    id: int
    name: str
    job: str | None = None 
    age: int | None = None 
    create_dtm: datetime

    # this is necessary for sqlalchemy to convert to BaseModel
    class Config:
        orm_mode = True