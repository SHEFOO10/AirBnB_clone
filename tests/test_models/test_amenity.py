#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_AmenityModel(test_basemodel):
    """ test Amenity Model """
    def __init__(self, *args, **kwargs):
        """ Initiate Amenity Test Class """
        super().__init__(*args, **kwargs)
        self.classname = 'Amenity'
        self.value = Amenity()

    def test_name_is_present(self):
        """ test if name is present """
        instance = self.value
        self.assertIsInstance(instance.name, str)
