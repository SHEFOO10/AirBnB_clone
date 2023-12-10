#!/usr/bin/python3
""" Test file for base_model to test it's functions """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_basemodel(unittest.TestCase):
    """ test cases for BaseModel """
    def test_instanciation_without_args(self):
        """ make new instance"""
        instance = BaseModel()
        self.assertEqual(instance.id, instance.id)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_instanciation_with_args(self):
        """ make new instance with args """
        first_instance = BaseModel()
        second_instance = BaseModel(**first_instance.to_dict())
        self.assertEqual(first_instance.id, second_instance.id)
        self.assertEqual(first_instance.updated_at, second_instance.updated_at)
        self.assertEqual(first_instance.created_at, second_instance.created_at)
        self.assertFalse(second_instance.__class__ == str)

    def test_instanciation_with_invalid_args(self):
        """ make new instance with invalid args """
        with self.assertRaises(TypeError):
            instance = BaseModel(**{1: 1})

    def test_print_basemodel(self):
        """
        check if str representation of basemodel
        matching the pattern [<class name>] (<self.id>) <self.__dict__>
        """
        instance = BaseModel()
        pattern = (
            r"\[\w+\] "    # Model Name
            r"\([0-9a-z-]+\) "    # uuid
            r"\{('\w+': (UUID\('[0-9a-z-]+'\)|'.+'|\w+\.\w+\(.+\))"  # dict
            r"(, )?)+\}"  # comma between elements
            )
        self.assertRegex(instance.__str__(), pattern)

    def test_save(self):
        """ test save function """
        instance = BaseModel()
        old_update_at = str(instance.updated_at)
        instance.save()
        self.assertNotEqual(old_update_at, str(instance.updated_at))

    def test_todict(self):
        """ test converting object to dictionary """
        instance = BaseModel()
        self.assertIsInstance(instance.to_dict(), dict)
        self.assertTrue('__class__' in instance.to_dict().keys())
        self.assertIsInstance(instance.to_dict()['created_at'], str)
        self.assertIsInstance(instance.to_dict()['updated_at'], str)
