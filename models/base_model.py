#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import models
import uuid as uid
from datetime import datetime as dt

"""
This is a Python class that will be the Base class or Parent class from which
all other classes will inherit from.
"""


class BaseModel():
    """
    This is a class modelling the BaseModel object for AirBnB Clone project.
    """
    def __init__(self, *args, **kwargs) -> None:
        """This is the constructor for the BaseModel class that instantiates
        an instance of the BaseModel object when created.

        Args:
            args (any) - non-keyworded arguments
            kwargs (any) - keyworded key and valued paired arguments
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, dt.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """Public instance method for the BaseModel that returns a String
        Representation of our BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """Public instance method that updates the `updated_at` public
        instance property"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        data = {}
        # iterate over all attributes of the object
        for attr in self.__dict__:
            key = attr
            # get the value of the attribute
            value = getattr(self, attr)
            # convert to string object in ISO format
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            # collect data for serializable attributes
            data[key] = value
            # add the key __class__ with the name of the class object
            data['__class__'] = self.__class__.__name__
        return data
