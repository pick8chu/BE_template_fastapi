from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
import config.constants as CONSTANTS

SQLALCHEMY_DATABASE_URI = f"postgresql://{CONSTANTS.DB_USER_NAME}:{CONSTANTS.DB_PASSWORD}@localhost:5432/{CONSTANTS.DB_DATABASE}"
SQLALCHEMY_TEST_DATABASE_URI = f"postgresql://{CONSTANTS.DB_USER_NAME}:{CONSTANTS.DB_PASSWORD}@localhost:5432/test_db"

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
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
# autocommit = True to connect several methods in one session.
# if those several methods commit their changes on their scope, when something has failed
# some of them were committed and the others were not.

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()