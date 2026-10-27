#!/usr/bin/python3

"""
Makes a class that represents a state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    The state object
    """

    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
