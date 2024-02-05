#!/usr/bin/python3

"""
Module containing the FileStorage class
"""
import json
import os.path as path


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
        # key = "{0}.{1}".format(obj['__class__'], obj['id'])
        # self.__objects.update({key: obj})
        print("type of object: {0}\nstring of object: {1}".format(type(obj), obj))

    def save(self):
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                if path.getsize(self.__file_path) > 0:
                    self.__objects = json.loads(file.read())
