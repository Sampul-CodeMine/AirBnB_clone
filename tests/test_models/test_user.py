#!/usr/bin/python3
"""Class to Perform Test on User Object"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Testuser(unittest.TestCase):

    def test_User(self):
        """
        Test attributes of Class User
        """
        new_user = User()
        new_user.first_name = 'Test'
        new_user.last_name = 'Admin'
        new_user.email = 'tester@oop.com'
        self.assertEqual(new_user.first_name, 'Test')
        self.assertEqual(new_user.last_name, 'Admin')
        self.assertEqual(new_user.email, 'tester@oop.com')
