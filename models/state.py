#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ as env
from models.base_model import BaseModel, Base
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State"""
    __tablename__ = "states"
    cities = relationship("City", cascade="all, delete", backref="state")
    name = Column(String(128), nullable=False)

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of City"""
            all = [
                v for k, v in models.storage.all(models.City).items()
                if v.state_id == self.id
            ]
            return (all)
