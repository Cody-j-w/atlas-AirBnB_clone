#!/usr/bin/python3

from .base_model import BaseModel
from . import storage

class User(BaseModel):
    """
    """

    def __init__(self, email, pwd, first, last):
        super().__init__()
        self.email = email
        self.password = pwd
        self.first_name = first
        self.last_name = last
        storage.new(self.to_dict())