#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a Python class that models a Place class but inherits from the
BaseModel class as the Parent Class
"""


class Place(BaseModel):
    """
    This is a class modelling the Place object for AirBnB Clone project.
    """
    amenity_ids = []
    city_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    name = ""
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    user_id = ""
