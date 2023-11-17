#!/usr/bin/python3
"""
This script defines a State class and a Base class
to work with sqlalchemy ORM
"""

from sqlalchemy import Columns, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class

    Attributes:
        __tablename__ (str): the name of the table
        id (int): state id
        name (str) the state name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
