#!/usr/bin/python3

"""This Module houses the function that list all cities
safely and takes a name from the command execution argument

"""

import sys
import MySQLdb


def city_name():
    """Print all cities from the cities table"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    port_n = 3306

    db = MySQLdb.connect(host='localhost', passwd=password, db=database,
                         port=port_n, user=username)
    cur = db.cursor()

    cur.execute("SELECT cities.name\
    FROM cities\
    WHERE cities.state_id = (\
    SELECT id FROM states WHERE BINARY name = %s LIMIT 1)\
    ORDER BY cities.id ASC", (state_name,))

    for data in cur.fetchall():
        print(data)
    cur.close()
    db.close()


if __name__ == '__main__':
    city_name()
