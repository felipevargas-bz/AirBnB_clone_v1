#!/usr/bin/python
"""
Unitest base model
"""
from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """
    Class test
    """
    def test_id(self):
        object1 = BaseModel()
        object2 = BaseModel()
        object1.name = "prueba"
        self.assertEqual(object1.name, "prueba")
        self.assertNotEqual(object1.id, object2.id)

    def test_created(self):
        object1 = BaseModel()
        object2 = BaseModel()
        self.assertNotEqual(object1.created_at, object2.created_at)
        self.assertNotEqual(object1.updated_at, object2.updated_at)
        self.assertNotEqual(object1.created_at, object1.updated_at)
        self.assertNotEqual(object2.created_at, object2.updated_at)

    def test_to_dict(self):
        object1 = BaseModel()
        object2 = object1.to_dict()
        self.assertEqual(object2["updated_at"], object1.to_dict["updated_at"])
