#!/usr/bin/python3

"""This module creates a function that list all
states with a name as the last argument of the command

It will do it safely
"""

import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import select


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
    query = session.query(State.id, State.name).first()
    if (query is not None):
        print(str(query.id) + ": " + str(query.name))
    else:
        print()


if __name__ == "__main__":
    name_states()
