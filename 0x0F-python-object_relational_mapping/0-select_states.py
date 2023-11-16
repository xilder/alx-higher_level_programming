#!/usr/bin/python3
"""lists all the states from the pased database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Accesses the and prints the rows in the states table"""
    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    row_state = cursor.fetchall()

    for row in row_state:
        print(row)
