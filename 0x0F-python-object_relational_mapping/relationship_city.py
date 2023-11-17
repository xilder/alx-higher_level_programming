#!/usr/bin/python3
"""
City class defined by the SQLalchemy module
"""

from relationship_state import Base, State
from sqlalchemy import ForeignKey, Column, Integer, String


class City(Base):
    """
    City class

    Attributes:
        __tablename__ (str): name of the table
        id (int): id of the class
        name (str): name of the city
        state_id (int): foreign key relating to the stae id
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
