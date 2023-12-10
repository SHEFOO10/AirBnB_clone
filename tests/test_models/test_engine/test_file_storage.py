#!/usr/bin/python3
""" this file holds Test_filestorage class to test filestorage functions """
import unittest
from models.engine.file_storage import FileStorage
from models import storage, base_model
import os
import json


class Test_filestorage(unittest.TestCase):
    """ test FileStorage class and it's tests """

    def setUp(self):
        """ before every test it reload storage """
        storage.reload()

    def tearDown(self):
        """after every test it deletes file.json if it exists """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_private_attributes(self):
        """ check if attributes is truely private """
        with self.assertRaises(AttributeError):
            storage.__file_path
        with self.assertRaises(AttributeError):
            storage.__objects

    def test_all(self):
        """ test all function that returns all objects in FileStorage """
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """ test new function that add new object to __object dictionary """
        instance = base_model.BaseModel()
        instance.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save(self):
        """ save __objects into json file """
        instance = base_model.BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            content = f.read()
            self.assertTrue(content != '')
            content = json.loads(content)
            self.assertIsInstance(content, dict)

    def test_reload(self):
        """
        test reload function
            that deserializes the json file to __objects
        """
        instance = base_model.BaseModel()
        instance.save()
        key = instance.__class__.__name__+'.'+instance.id
        storage.reload()
        self.assertTrue(storage.all()[key], instance)
        with open('file.json', 'r') as f:
            content = json.load(f)
            self.assertTrue(content[key]['id'] == instance.to_dict()['id'])
