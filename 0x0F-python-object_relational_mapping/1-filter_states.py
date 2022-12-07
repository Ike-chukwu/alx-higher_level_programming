#!/usr/bin/python3
""" This module filters all the states from the
    database hbtn_0e_0_usa that start with upper N.
"""

import MySQLdb
import sys


def main():
    """
        Function containing code to filter all the states
        from the database.
    """

    # Create a database connection
    conn = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    cur = conn.cursor()
    # Select states
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    [print(state) for state in query_rows if state[1][0] == "N"]
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
