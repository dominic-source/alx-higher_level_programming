#!/usr/bin/python3

"""This module creates a function that list all
states with a name as the last argument of the command
and contains the letter 'a'
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
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    data = session.query(State).filter(State.name.like("%a%"))
    data = data.order_by(State.id)
    for query in data:
        print(str(query.id) + ": " + str(query.name))


if __name__ == "__main__":
    name_states()
