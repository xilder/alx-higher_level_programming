#!/usr/bin/python3

"""
lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_city import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id)\
        .all()

    for city, state in cities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.add(state)
    session.commit()
    session.close()
