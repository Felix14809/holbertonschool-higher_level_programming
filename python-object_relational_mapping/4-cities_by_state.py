#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa."""


import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(
        host=MY_HOST,
        port=MY_PORT,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB
        )

    cursor = db.cursor()
    query = (
        """
        SELECT c.id, c.name, s.name
        FROM cities c
        LEFT JOIN states s ON c.state_id = s.id
        ORDER BY c.id
        """
        )
    cursor.execute(query)

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
