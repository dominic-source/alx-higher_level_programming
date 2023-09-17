#!/usr/bin/python3

"""This module creates a function that list all
states with a name as the last argument of the command

"""
import MySQLdb
import sys


def name_states():
    """list state that is name"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    port_n = 3306

    db = MySQLdb.connect(host='localhost', port=port_n, passwd=password,
                         db=database, user=username)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'\
    ORDER BY states.id ASC".format(state_name))
    for data in cur.fetchall():
        print(data)
    db.commit()
    cur.close()
    db.close()


if __name__ == "__main__":
    name_states()
