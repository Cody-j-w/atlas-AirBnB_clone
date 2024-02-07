#!/usr/bin/python3

"""
Module containing the City class
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    City class, inheriting from BaseModel

    Attributes:
        state_id: string - the instance id of the state where the city is
        located
        name: string - the name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
