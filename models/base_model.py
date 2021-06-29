#!/usr/bin/python3
"""
BaseModel Module
"""
from uuid import uuid4
from datetime import *
import models

formt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """
    Base class model that will define all common
    attributes/methods for other classes

    public instance attributes:
        id: type string (unique id)
        created_at : creation date
        updated_at : last modification date
    Public instance methods:
        def save(): save last time object modification
        def to_dict(): returns a dictionary containing all instances
    """

    def __init__(self, *args, **kwargs):
        """
        Initializate object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if hasattr(self, "created_at") and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs["created_at"], formt)
                if hasattr(self, "update_at") and type(self.update_at) is str:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], formt)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """        
        Return object representation in human lenguaje
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        save the objects
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary whit all keys/values of instance
        """
        name = self.__class__.__name__
        new_dict = self.__dict__.copy()

        new_dict.update(__class__=name, created_at=self.created_at.isoformat())

        new_dict.update(updated_at=self.updated_at.isoformat())

        return new_dict
