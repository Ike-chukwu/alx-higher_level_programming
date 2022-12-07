#!/usr/bin/python3
"""Defines a city model
    Inherits from the SQLAlchemy Base and links to the MYSQL cities table.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """ Represents a city for a MYSQL database.
    id (sqlalchemy.Integer): The cities id.
    name (sqlalchemy.String): The name of the city.
    state_id(sqlalchemy,Integer): Foreign key to states_id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states_id"), nullable=False)
