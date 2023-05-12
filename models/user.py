#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a Python class that models a User class but inherits from the
BaseModel class as the Parent Class
"""


class User(BaseModel):
    """
    This is a class modelling the User object for AirBnB Clone project.
    """
    email = ""
    first_name = ""
    last_name = ""
    password = ""
