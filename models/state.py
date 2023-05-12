#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a Python class that models a State class but inherits from the
BaseModel class as the Parent Class
"""


class State(BaseModel):
    """
    This is a class modelling the State object for AirBnB Clone project.
    """
    name = ""
