#!/usr/bin/python3

"""This module create a function that will print all cities

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, subqueryload
import sys
from model_state import Base
from model_city import City, State


def print_cities():
    """This will print all the cities"""

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    port_n = 3306
    url = "mysql+mysqldb://{}:{}@localhost:{}/{}".format(username,
                                                         password,
                                                         port_n, db)
    engine = create_engine(url)
    Base = declarative_base()
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    for state, city in session.query(State, City).join(State.cities).all():
        print("{}: ({}) {}".format(state.name, city.id,
                                   city.name))


if __name__ == '__main__':
    print_cities()
