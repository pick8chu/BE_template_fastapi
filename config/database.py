from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
import config.constants as CONSTANTS

SQLALCHEMY_DATABASE_URI = f"postgresql://{CONSTANTS.DB_USER_NAME}:{CONSTANTS.DB_PASSWORD}@localhost:5432/{CONSTANTS.DB_DATABASE}"

'''
TEST TABLE CREATION SQL IS BELOW
-------------------------------------------------

CREATE SEQUENCE test_id_sequence;

CREATE TABLE public.test_mt (
	id numeric NOT null primary key
			DEFAULT nextval('test_id_sequence'),
	"name" varchar NULL,
	job varchar NULL,
	age numeric NULL,
	create_dtm timestamptz NULL DEFAULT now()
);

'''
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()