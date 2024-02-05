#!/usr/bin/python3

"""
Module containing the Amenity class
"""

from .base_model import BaseModel
from . import storage


class Amenity(BaseModel):
    """
    Amenity class, inheriting from BaseModel

    Attributes:
        name: string - the name of the amenity
    """

    name = ""
    def __init__(self):
        super().__init__()
