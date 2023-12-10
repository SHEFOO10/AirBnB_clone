#!/usr/bin/python3
""" this file hold BaseModel Class with it's functions """
import uuid
from datetime import datetime


class BaseModel():
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initiate BaseModel object """
        from models import storage
        if kwargs is None or kwargs == {} or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.update(**kwargs)

    def __str__(self):
        """ return the string representation of the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def update(self, **kwargs):
        """ update object with given dictionary """
        del kwargs['__class__']
        for attribute, value in kwargs.items():
            if attribute == 'created_at' or attribute == 'updated_at':
                setattr(self, attribute,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            else:
                setattr(self, attribute, value)

    def save(self):
        """ save the object """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

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
