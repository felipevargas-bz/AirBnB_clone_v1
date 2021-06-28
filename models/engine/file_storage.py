#!/usr/bin/python3


import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}



    def all(self):
        """
        return the dicctinary of __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__clas__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(objects, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        pass
