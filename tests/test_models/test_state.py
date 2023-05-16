#!/usr/bin/python3
"""Class to Perform Test on State Object"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Teststate(unittest.TestCase):

    def test_class(self):
        new_state = State()
        self.assertEqual(new_state.__class__.__name__, "State")

    def test_container(self):
        new_state = State()
        self.assertEqual(new_state.__class__.__name__, "State")

    def test_state(self):
        """
        Test attributes of State Object
        """
        new_state = State()
        new_state.name = "Lagos"
        self.assertEqual(new_state.name, 'Lagos')
