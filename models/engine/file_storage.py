#!/usr/bin/python3

"""
Module containing the FileStorage class
"""
import json
from os.path import isfile


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
        key = "{0}.{1}".format(obj['__class__'], obj['id'])
        self.__objects.update({key: obj})

    def save(self):
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read())
