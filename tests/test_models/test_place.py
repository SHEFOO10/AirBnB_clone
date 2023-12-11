#!/usr/bin/python3
""" Test Place Model """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_PlaceModel(test_basemodel):
    """ test Place Model """
    def __init__(self, *args, **kwargs):
        """ initiate Place Test Model """
        super().__init__(*args, **kwargs)
        self.classname = 'Place'
        self.value = Place()

    def test_cityId_is_present(self):
        """ test if city_id is present """
        instance = self.value
        self.assertIsInstance(instance.city_id, str)

    def test_userId_is_present(self):
        """ test if user_id is present """
        instance = self.value
        self.assertIsInstance(instance.user_id, str)

    def test_name_is_present(self):
        """ test if name is present """
        instance = self.value
        self.assertIsInstance(instance.name, str)

    def test_description_is_present(self):
        """ test if description is present """
        instance = self.value
        self.assertIsInstance(instance.description, str)

    def test_numberRooms_is_present(self):
        """ test if number_rooms is present """
        instance = self.value
        self.assertIsInstance(instance.number_rooms, int)

    def test_numberBathrooms_is_present(self):
        """ test if number_bathrooms is present """
        instance = self.value
        self.assertIsInstance(instance.number_bathrooms, int)

    def test_maxGuest_is_present(self):
        """ test if max_guest is present """
        instance = self.value
        self.assertIsInstance(instance.max_guest, int)

    def test_priceByNight_is_present(self):
        """ test if price_by_night is present """
        instance = self.value
        self.assertIsInstance(instance.price_by_night, int)

    def test_latitude_is_present(self):
        """ test if latitude is present """
        instance = self.value
        self.assertIsInstance(instance.latitude, float)

    def test_longitude_is_present(self):
        """ test if latitude is present """
        instance = self.value
        self.assertIsInstance(instance.latitude, float)

    def test_amenityIds_is_present(self):
        """ test if amenity_ids present and holds list of strings """
        instance = self.value
        self.assertIsInstance(instance.amenity_ids, list)
        [self.assertIsInstance(item, str) for item in instance.amenity_ids]
