#!/usr/bin/python3
"""Class to Perform Test on Review Object"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Testreview(unittest.TestCase):

    def test_class(self):
        my_review = Review()
        self.assertEqual(my_review.__class__.__name__, "Review")

    def test_father(self):
        my_review = Review()
        self.assertTrue(issubclass(my_review.__class__, BaseModel))

    def test_review(self):
        """
        Test our Review Class
        """
        new_place = Place()
        new_user = User()
        my_review = Review()
        my_review.place_id = new_place.id
        my_review.user_id = new_user.id
        my_review.text = 'holberton'
        self.assertEqual(my_review.place_id, new_place.id)
        self.assertEqual(my_review.user_id, new_user.id)
        self.assertEqual(my_review.text, 'holberton')
