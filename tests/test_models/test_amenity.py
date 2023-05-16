#!/usr/bin/python3
"""Class to Perform Test on Amenity Object"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class Testamenity(unittest.TestCase):

    def test_class(self):
        new_amnty = Amenity()
        self.assertEqual(new_amnty.__class__.__name__, "Amenity")

    def test_father(self):
        new_amnty = Amenity()
        self.assertTrue(issubclass(new_amnty.__class__, BaseModel))

    def test_amenity(self):
        """Test attributes of Class Amenity"""
        new_amnty = Amenity()
        new_amnty.name = "Free Health Care"
        self.assertEqual(new_amnty.name, 'Free Health Care')
