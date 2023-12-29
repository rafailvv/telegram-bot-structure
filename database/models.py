# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TestTable(Base):
    __tablename__ = "students_iu"

    id = Column(Integer, primary_key=True)
    test_text = Column(String(100))
