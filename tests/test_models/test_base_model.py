#!/usr/bin/python3
"""
Test suits for the base model
"""

import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test class
    """

    def setUp(self):
        """
        Classes needed for testing
        """
        pass

    def test_init(self):
        """
        Test the constructor
        """
        my_model = BaseModel()
        self.assertTrue(type(my_model.id), str)
        self.assertTrue(len(my_model.id), 36)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)
        self.assertEqual(my_model.updated_at, my_model.created_at)

    def test_str_rep(self):
        """
        Test the str representation
        """
        my_model = BaseModel()
        my_model.name = "Alx"
        my_model.my_number = 89
        self.assertEqual(str(my_model), '[{}] ({}) {}'.format(
            my_model.__class__.__name__,
            my_model.id,
            my_model.__dict__))

    def test_updated_time(self):
        """
        Check if updated time is changed when new attributes created
        """
        my_model = BaseModel()
        my_model.name = "Alx"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(my_model.updated_at, my_model.created_at)

    def test_kwargs(self):
        """
        Test init with kwargs
        """
        my_model = BaseModel()
        my_model.name = "Alx"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertNotEqual(str(my_model), str(my_new_model))
        self.assertFalse(my_model is my_new_model)


if __name__ == '__main__':
    unittest.main()
