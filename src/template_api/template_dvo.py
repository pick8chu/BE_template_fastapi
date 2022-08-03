# from decimal import Decimal
# from msilib import sequence
from sqlalchemy import Column, Sequence, ForeignKey, Integer, String, Float, BigInteger, DateTime, Date, Numeric, Boolean, Text, BigInteger, null
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.database import Base

seq = Sequence('test_id_sequence')

class Person(Base):
    __tablename__ = "test_mt"

    id = Column(Integer, seq, server_default=seq.next_value(), primary_key=True)
    name = Column(String(30))
    job = Column(String(20))
    age = Column(Integer)
    create_dtm = Column(DateTime, server_default="now()")