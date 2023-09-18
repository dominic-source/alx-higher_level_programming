#!/usr/bin/python3

"""This module create a class defination ORM

"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from relationship_state import Base


class City(Base):
    """This is the base class for cities"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
