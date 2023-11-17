#!/usr/bin/python3
"""
that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_city import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    that prints all City objects from the database hbtn_0e_14_usa
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states = session.query(City, State).filter(
            City.state_id == State.id).all()

    if cities_states is not None:
        for city, state in cities_states:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
