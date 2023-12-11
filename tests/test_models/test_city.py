#!/usr/bin/python3
""" test city Model """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_CityModel(test_basemodel):
    """ test_CityModel """
    def __init__(self, *args, **kwargs):
        """ Initiate CityModel Class """
        super().__init__(*args, **kwargs)
        self.classname = 'City'
        self.value = City()

    def test_state_id_is_present(self):
        """ test if state_id is present """
        instance = self.value
        self.assertIsInstance(instance.state_id, str)

    def test_name_is_present(self):
        """ test if name is present """
        instance = self.value
        self.assertIsInstance(instance.name, str)
