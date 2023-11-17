#!/usr/bin/python3
"""gets cities by state"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """gets cities by state"""

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute('SELECT cities.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %(name)s\
            ORDER BY cities.id ASC', {'name': argv[4]})
    row_cities = cursor.fetchall()

    if row_cities is not None:
        print(', '.join([city[0] for city in row_cities]))
