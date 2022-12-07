#!/usr/bin/python3
""" This module takes the name of a state as argument and displays all cities
    of that state, using the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def main():
    """
        Entry point to the program:
        creates a database connection and performs operations on
        the databse.
    """

    # Create a database connection
    conn = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    cur = conn.cursor()
    # Select states
    state_name = sys.argv[4]
    cur.execute(
            "SELECT name FROM cities WHERE state_id IN\
            (SELECT id FROM states WHERE name = %s)\
            ORDER BY cities.id", (state_name, ))
    query_rows = cur.fetchall()
    print(', '.join([x[0] for x in query_rows]))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
