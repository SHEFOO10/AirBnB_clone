#!/usr/bin/python3
""" this file hold BaseModel Class with it's functions """
import uuid
from datetime import datetime


class BaseModel():
    """ defines all common attributes/methods for other classes """
    def __init__(self):
        """ Initiate BaseModel object """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ return the string representation of the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save the object """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return the object as dictionary """
        new_dictionary = {key: value for key, value in self.__dict__.items()}
        new_dictionary.update({'__class__': self.__class__.__name__})
        new_dictionary.update(
            {'created_at': datetime.isoformat(new_dictionary['created_at'])}
            )
        new_dictionary.update(
            {'updated_at': datetime.isoformat(new_dictionary['updated_at'])}
            )
        return new_dictionary
