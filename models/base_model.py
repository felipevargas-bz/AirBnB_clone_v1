#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    parent class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Contructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string"""
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def to_dict(self):
        """Return dictionary"""
        new_dic = {'updated_at': self.updated_at.isoformat(),
                   'created_at': self.created_at.isoformat(),
                   '__class__': self.__class__.__name__}
        return dict(self.__dict__, **new_dic)

    def save(self):
        """save funtion to update the time"""
        self.updated_at = datetime.now()
        models.storage.save()
