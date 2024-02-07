#!/usr/bin/python3

"""
Module containing the Amenity class
"""

from .base_model import BaseModel



class Amenity(BaseModel):
    """
    Amenity class, inheriting from BaseModel

    Attributes:
        name: string - the name of the amenity
    """

    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
