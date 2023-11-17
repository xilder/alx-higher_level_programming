#!/usr/bin/python3
"""a safe method to query the sql database based on 2-my_filter_states.py"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """a safe method to query the sql database, 2-my_filter_states.py"""

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states\
                WHERE name = %(name)s\
                ORDER BY name ASC', {'name': argv[4]}
                )
    row_states = cursor.fetchall()

    for state in row_states:
        print(statc)
