#!/usr/bin/python3
""" Defines BaseModel class """
import uuid
from datetime import datetime


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self):
        """ Initialize instances """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns string representation of instance """
        str_rep = "[{}] ({}) {}"
        cls_name = __class__.__name__
        return (str_rep.format(cls_name, self.id, self.__dict__))

    def save(self):
        """ Updates updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all key/values
            of __dict__ of an instance
        """
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
