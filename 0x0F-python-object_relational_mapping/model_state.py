#!/usr/bin/python3

"""This module create a class defination ORM

"""

from sqlalchemy import String, Column, Table, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()


class State(Base):
    """This is the base class for states"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
