from decimal import Decimal
from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger, DateTime, Date, Numeric, Boolean, Text, BigInteger, null
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.database import Base

class Person(Base):
    __tablename__ = "test_mt"

    id = Column(Numeric, primary_key=True, server_default="nextval('test_id_sequence')")
    name = Column(String(30))
    job = Column(String(20))
    age = Column(Numeric)
    create_dtm = Column(DateTime, server_default="now()")