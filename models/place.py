#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('amenity_id', String(60), ForeignKey("amenities.id"))
    Column('place_id', String(60), ForeignKey("places.id")),
)


class Place(BaseModel):
    """ A place to stay"""

    __tablename__ = "places"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    amenity_ids = []
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place",
        viewonly=False
    )

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get all reviews with the current place id"""
            all = [
                v for k, v in models.storage.all(models.Review).items()
                if v.place_id == self.id
            ]
            return (all)

        @property
        def amenities(self):
            """Get all amenities with the current place id"""
            all = [
                v for k, v in models.storage.all(models.Amenity).items()
                if v.id in self.amenity_ids
            ]
            return (all)
