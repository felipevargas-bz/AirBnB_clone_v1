#!/usr/bin/python3
""" Module for class City that
inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of city """
    state_id = ""
    name = ""
