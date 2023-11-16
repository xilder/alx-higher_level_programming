#!/usr/bin/python3
"""Prints all states beginning with 'N' in the given database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Gets the required state"""

    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states\
            WHERE name LIKE BINARY "N%"\
            ORDER BY id ASC')
    row_states_N = cursor.fetchall()

    for state in row_states_N:
        print(state)
