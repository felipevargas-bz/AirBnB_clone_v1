#!/usr/bin/python3


import json


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dicctinary of __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except:
            pass
