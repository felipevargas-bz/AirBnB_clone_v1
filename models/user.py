#!/usr/bin/python3
""" Module for class User that
inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
