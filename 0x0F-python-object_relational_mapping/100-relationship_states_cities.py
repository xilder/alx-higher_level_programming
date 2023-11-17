#!/usr/bin/python3

"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_city import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()


