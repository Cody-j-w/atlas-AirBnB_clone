#!/usr/bin/python3

"""
A module containing the User class
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    The User class, inheriting from BaseModel

    Attributes:
        email: string - the User's email address
        password: string - the User's password
        first_name: string - the User's first name
        last_name: string - the User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
