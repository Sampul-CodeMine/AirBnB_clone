""" Defines test cases for BaseModel class  """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import uuid


class TestBaseModelClass(unittest.TestCase):
    """ Test cases for BaseModel class """

    @classmethod
    def setUpClass(cls):
        """ Set up class instances """
        cls.first_model = BaseModel()
        cls.second_model = BaseModel()

    def test_unique_id(self):
        """ Test for unique id of each class instance """
        self.assertNotEqual(self.first_model.id, self.second_model.id)

    def test_instance_of_datetime(self):
        """
            Test that the created_at and updated_at attributes
            are instances of datetime
        """
        # for created_at attribute
        self.assertIsInstance(self.first_model.created_at, datetime)
        self.assertIsInstance(self.second_model.created_at, datetime)
        # for updated_at attribute
        self.assertIsInstance(self.first_model.updated_at, datetime)
        self.assertIsInstance(self.second_model.updated_at, datetime)

    def test_str_method(self):
        """
           Test that the str method returns a string in the
           format '[<class name>] (<self.id>) <self.dict>'
        """
        expected_output = (
            f"[{type(self.first_model).__name__}] "
            f"({self.first_model.id}) "
            f"{self.first_model.__dict__}"
        )
        self.assertEqual(str(self.first_model), expected_output)

    def test_save_method(self):
        """
           Test that the save method updates the
           updated_at attribute to the current datetime
        """
        initial = self.first_model.updated_at
        updated = self.first_model.save()
        self.assertNotEqual(initial, updated)

    def test_to_dict_method(self):
        """
           Test that the to_dict method returns a dictionary
           representation of the object with all instance attributes set
        """
        self.assertIsInstance(self.first_model.to_dict(), dict)

    def test_ISO_format(self):
        """
           Test that the created_at and updated_at attributes
           are converted to string objects in the ISO format specified.
           It makes use of regular expression to match the pattern.
        """
        obj = self.first_model.to_dict()
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}"
        self.assertRegex(str(obj['created_at']), pattern)
        self.assertRegex(str(obj['updated_at']), pattern)

    def test_recreate_instance(self):
        """
           Test that an instance is re-created from its
           dictionary representaion
        """
        obj_json = self.first_model.to_dict()
        new_obj = BaseModel(**obj_json)
        self.assertIsNot(obj_json, new_obj)
