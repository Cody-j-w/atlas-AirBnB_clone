#!/usr/bin/python3

"""
Module containing Review class
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class, inheriting from BaseModel

    Attributes:
        place_id: string - the id of the Place being reviewed
        user_id: string - the id of the User making the Review
        text: string - the body of the Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
