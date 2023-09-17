#!/usr/bin/python3

"""This module creates a function that will add a new state

"""

import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData


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
    new_user = State(name="Louisiana")
    session.add(new_user)
    session.commit()
    print(new_user.id)


if __name__ == "__main__":
    name_states()
