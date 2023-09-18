#!/usr/bin/python3

"""This module creates a function that will manipulate state and city models

"""

import sys
from sqlalchemy.orm import Session, relationship
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base


def name_states():
    """list state that is name"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port_n = 3306

    url = "mysql+mysqldb://{}:{}@localhost:{}/{}".format(username,
                                                         password,
                                                         port_n,
                                                         database)

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.commit()


if __name__ == "__main__":
    name_states()
