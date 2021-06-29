#!/usr/bin/python3


import json
from models.base_model import BaseModel


list_of_class_in_dict = {"BaseModel": BaseModel}

class FileStorage():

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
        if obj is not None:
            key = obj.__class__.__name__+'.' + obj.id
            self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        j_objects = {}
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                f_json = json.load(file)
                for key in f_json:
                    self.__objects[key] = list_of_class_in_dict[f_json[key]\
                        ["__class__"]](**f_json[key])
        except:
            pass
