#!/usr/bin/python3

"""
Module containing the FileStorage class
"""
import json
import os.path as path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class, provides a system of storing data in a JSON file

    Attributes:
        __objects: list - the list of objects currently stored in a FileStorage
        instance
        __file_path: string - the path to the longterm storage file
    """
    __objects = {}
    __file_path = "storage.json"

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{0}.{1}".format(type(obj).__name__, obj.id)
        self.__objects.update({key: obj})



    def save(self):
        obj_dict = dict()
        for key, value in self.__objects.items():
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(obj_dict))

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                content = json.loads(file.read())
            for key, value in content.items():
                self.__objects[key] = eval(key.split(".")[0])(**value)
