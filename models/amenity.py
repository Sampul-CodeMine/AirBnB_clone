#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a Python class that models an Amenity class but inherits from
the BaseModel class as the Parent Class
"""


class Amenity(BaseModel):
    """
    This is a class modelling the Amenity object for AirBnB Clone project.
    """
    name = ""
