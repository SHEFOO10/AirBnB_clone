#!/usr/bin/python3
""" Holds tests for User Model """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test User class attributes type"""

    def __init__(self, *args, **kwargs):
        """ Initiate Test User class """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User()

    def test_first_name(self):
        """ test type of first_name attribute"""
        new = self.value
        self.assertIsInstance(new.first_name, str)

    def test_last_name(self):
        """ test type of last_name attribute """
        new = self.value
        self.assertIsInstance(new.last_name, str)

    def test_email(self):
        """ test type of email attribute """
        new = self.value
        self.assertIsInstance(new.email, str)

    def test_password(self):
        """ test type of password attribute """
        new = self.value
        self.assertIsInstance(new.password, str)
