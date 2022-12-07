#!/usr/bin/python3
""" This module lists all the states from the
    database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
        Function containing code to select all the states
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
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
