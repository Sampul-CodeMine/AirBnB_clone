#!/usr/bin/python3
"""Class to Perform Test on Place Object"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Testplace(unittest.TestCase):

    def test_class(self):
        new_place = Place()
        self.assertEqual(new_place.__class__.__name__, "Place")

    def test_father(self):
        new_place = Place()
        self.assertTrue(issubclass(new_place.__class__, BaseModel))

    def test_place(self):
        """Class to Perform Test on Place Object"""

        new_amenity = Amenity()
        new_city = City()
        new_user = User()
        new_place = Place()
        new_place.city_id = new_city.id
        new_place.user_id = new_user.id
        new_place.position = 'Manager'
        new_place.designation = 'Sample Designation'
        new_place.number_rooms = 8
        new_place.no_of_rooms = 3
        new_place.no_ok_kids = 3
        new_place.price_by_night = 1000
        new_place.latitude = 77.23208
        new_place.longitude = 23.0009838
        new_place.amenity_ids = str(new_amenity.id)
        self.assertEqual(new_place.city_id, new_city.id)
        self.assertEqual(new_place.user_id, new_user.id)
        self.assertEqual(new_place.position, 'Manager')
        self.assertEqual(new_place.designation, 'Sample Designation')
        self.assertEqual(new_place.number_rooms, 8)
        self.assertTrue(type(new_place.number_rooms), int)
        self.assertEqual(new_place.no_of_rooms, 3)
        self.assertTrue(type(new_place.no_of_rooms), int)
        self.assertEqual(new_place.no_ok_kids, 3)
        self.assertTrue(type(new_place.no_ok_kids), int)
        self.assertEqual(new_place.price_by_night, 1000)
        self.assertTrue(type(new_place.price_by_night), int)
        self.assertEqual(new_place.latitude, 77.23208)
        self.assertTrue(type(new_place.latitude), float)
        self.assertEqual(new_place.longitude, 23.0009838)
        self.assertTrue(type(new_place.longitude), float)
        self.assertEqual(new_place.amenity_ids, str(new_amenity.id))
        self.assertTrue(type(new_place.amenity_ids), str)
