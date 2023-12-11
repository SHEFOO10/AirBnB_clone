#!usr/bin/python3
""" test State Class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_stateModel(test_basemodel):
    """ Test state Class """
    def __init__(self, *args, **kwargs):
        """ Initiate test_stateModel class """
        super().__init__(*args, **kwargs)
        self.classname = 'State'
        self.value = State()

    def test_name_is_present(self):
        """ test if name class attribute is present """
        instance = self.value
        self.assertIsInstance(instance.name, str)
