#!/usr/bin/python3
""" test Review Model """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_ReviewModel(self):
    """ test review model """
    def __init__(self, *args, **kwargs):
        """ Initiate Review Test Model """
        super().__init__(*args, **kwargs)
        self.classname = 'Review'
        self.value = Review()

    def test_placeId_is_present(self):
        """ test if place_id is present """
        instance = self.value
        self.assertIsInstance(instance.place_id, str)

    def test_userId_is_present(self):
        """ test if place_id is present """
        instance = self.value
        self.assertIsInstance(instance.user_id, str)

    def test_text_is_present(self):
        """ test if text is present """
        instance = self.value
        self.assertIsInstance(instance.text, str)
