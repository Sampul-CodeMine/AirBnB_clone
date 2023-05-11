#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import json
from models.base_model import BaseModel as bm

"""
This is a Python class that will be responsible for file storage. In this
class, objects will be serialized into a JSON string object and saved to a
flat database (json file)
"""


class FileStorage():
    """
    This is a class responsible for data storage for AirBnB Clone project.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ...

    def new(self):
        ...

    def save(self):
        ...

    def reload(self):
        ...