#!/usr/bin/python3

"""This module creates a function that will manipulate state and city models

"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City
from relationship_state import State

def name_states():
    """list state that is name"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port_n = 3306

    url = "mysql+mysqldb://{}:{}@localhost:{}/{}".format(username,
                                                         password, port_n,
                                                         database)
    engine = create_engine(url)
    session = Session(bind=engine)
    Base = declarative_base()
    Base.metadata.create_all(engine)
    ustate = State(name='California')
    ustate.cities = [City(name="San Francisco")]


if __name__ == "__main__":
    name_states()
