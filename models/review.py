#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import models
from os import getenv as env


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place",
        viewonly=False
    )

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """get all reviews with the current place id"""
            all = [
                v for k, v in models.storage.all(models.Review).items()
                if v.place_id == self.id
            ]
            return (all)

        @property
        def amenities(self):
            """get all amenities with the current place id"""
            all = [
                v for k, v in models.storage.all(models.Amenity).items()
                if v.id in self.amenity_ids
            ]
            return (all)
