#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a Python class that models a City class but inherits from the BaseModel
class as the Parent Class
"""


class City(BaseModel):
    """
    This is a class modelling the City object for AirBnB Clone project.
    """
    name = ""
    state_id = ""
