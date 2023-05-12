#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a Python class that models a Review class but inherits from the
BaseModel class as the Parent Class
"""


class Review(BaseModel):
    """
    This is a class modelling the Review object for AirBnB Clone project.
    """
    place_id = ""
    user_id = ""
    text = ""
