#!/usr/bin/python3
"""This module contains the code to lists all states from the database table

"""

import MySQLdb
import sys


def print_state():
    """The print_state module will print the state table"""

    database = sys.argv[3]
    password = sys.argv[2]
    username = sys.argv[1]
    port_n = 3306

    db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database, port=port_n)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")

    for data in cur:
        print(data)

if __name__ == '__main__':
    print_state()
