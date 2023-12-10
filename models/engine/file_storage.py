#!/usr/bin/python3
""" this file store File Storage Engine to store objects into json file """
import json


class FileStorage():
    """ define FileStorage and it's functions """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return all objects from the session """
        return self.__objects

    def new(self, obj):
        """ insert new object to objects dictionary """
        self.__objects[obj.__class__.__name__+'.'+obj.id] = obj

    def save(self):
        """ save objects into json file """
        with open(self.__file_path, 'w') as file:
            json.dump(
                {id: obj.to_dict() for id, obj in self.__objects.items()},
                file
                )

    def reload(self):
        """  deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        classes = {
            'BaseModel': BaseModel
        }
        try:
            with open(self.__file_path, 'r') as file:
                content = json.load(file)
            self.__objects = {
                key: classes[dictionary['__class__']](**dictionary)
                for key, dictionary in content.items()
                }
        except (FileNotFoundError):
            pass
