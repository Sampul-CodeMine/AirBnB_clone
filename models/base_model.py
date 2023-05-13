#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import uuid as uid
import models
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
        if kwargs != {} and kwargs is not None and bool(kwargs):
            for key in kwargs:
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = dt.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """Public instance method for the BaseModel that returns a String
        Representation of our BaseModel class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """Public instance method that updates the `updated_at` public
        instance property"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        data = self.__dict__.copy()
        data["__class__"] = type(self).__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data
