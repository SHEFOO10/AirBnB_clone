#!/usr/bin/python3
""" this file holds Test_filestorage class to test filestorage functions """
import unittest
from models.base_model import BaseModel
from models import storage
import os
import json


class Test_filestorage(unittest.TestCase):
    """ test FileStorage class and it's tests """

    def setUp(self):
        """ before every test delete objects stored in storage """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """after every test it deletes file.json if it exists """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_make_sure_no_jsonfile(self):
        """ just to make sure there's no file.json """
        self.assertFalse(os.path.exists('file.json'))

    def test_objects_is_empty(self):
        """ tests if __objects is empty """
        self.assertTrue(len(storage.all()) == 0)

    def test_instanciation_with_new_and_old(self):
        """ loading from json file and creating new object """
        old_instance = BaseModel()
        old_instance.save()
        new_instance = BaseModel(**old_instance.to_dict())
        self.assertTrue(os.path.getsize('file.json') > 0)

    def test_private_attributes(self):
        """ check if attributes is truely private """
        with self.assertRaises(AttributeError):
            storage.__file_path
        with self.assertRaises(AttributeError):
            storage.__objects

    def test_objects_type(self):
        """ check objects type """
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """ test all function that returns all objects in FileStorage """
        instance = BaseModel()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """ test new function that add new object to __object dictionary """
        instance = BaseModel()
        key = instance.__class__.__name__+'.'+instance.id
        self.assertTrue(storage.all()[key] is instance)
        self.assertTrue(len(storage.all()) == 1)

    def test_save(self):
        """ save __objects into json file """
        BaseModel().save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        test reload function
            that deserializes the json file to __objects
        """
        instance = BaseModel()
        instance.save()
        storage.reload()
        [self.assertTrue(obj.id == instance.id)
         for obj in storage.all().values()]

    def test_storage_var_isloaded(self):
        """ test if test variable is Not None and loaded correctlly """
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)

    def test_path_type(self):
        """ test if the path is not str """
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_key_format(self):
        """
        test if key format in storage is valid
        example: <classname>.<id>
        """
        new_instance = BaseModel()
        [self.assertEqual(key, 'BaseModel.' + new_instance.id)
         for key in storage.all().keys()]

    def test_reload_empty_jsonfile(self):
        """ test reload empty json file """
        with open(storage._FileStorage__file_path, 'w') as f:
            pass
        with open(storage._FileStorage__file_path, 'r') as f:
            with self.assertRaises(ValueError):
                storage.reload()

    def test_data_saved(self):
        """ tests if data is saved into json correctlly """
        new_instance = BaseModel()
        new_instance.save()
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_object_created_but_not_saved(self):
        """ make sure creating object won't affect in creating json file """
        new_instance = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_reload_from_nothing(self):
        """
        test storage reload which run pass
        if is there error in reloading
        """
        self.assertEqual(storage.reload(), None)
