#!/usr/bin/python3

"""
Module containing the State class
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    State class, inheriting from BaseModel

    Attributes:
        name: string - the state name
    """

    name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
