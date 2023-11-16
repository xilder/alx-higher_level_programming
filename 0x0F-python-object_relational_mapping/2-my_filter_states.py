#!/usr/bin/python3
"""Selects the states based on use input from a given database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """selects the state based on input"""

    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states\
            WHERE name = "{}"\
            ORDER BY id ASC'.format(argv[4])
            )
    row_state_input = cursor.fetchall()

    for state in row_state_input:
        print(state)
