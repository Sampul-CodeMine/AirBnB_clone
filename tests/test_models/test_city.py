#!/usr/bin/python3
"""Class to Perform Test on City Object"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Testcity(unittest.TestCase):

    def test_class(self):
        cty = City()
        self.assertEqual(cty.__class__.__name__, "City")

    def test_father(self):
        cty = City()
        self.assertTrue(issubclass(cty.__class__, BaseModel))

    def test_city(self):
        """
        Test attributes of Class City
        """
        new_city = City()
        new_state = State()
        new_city.name = "Ikeja"
        new_city.state_id = new_state.id
        self.assertEqual(new_city.name, 'Ikeja')
        self.assertEqual(new_city.state_id, new_state.id)
