#!/usr/bin/python3

"""

"""

import uuid
from datetime import datetime


class BaseModel:
    """

    """

    def __init__(self):
        timestr = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        name = type(self).__name__
        inst_dict = self.__dict__
        return "[{0}] ({1}) {2}".format(name, self.id, inst_dict)

    def to_dict(self):
        isocre = str(self.created_at.isoformat())
        isoupd = str(self.updated_at.isoformat())
        inst_dict = dict()
        for key, value in self.__dict__.items():
            inst_dict.update({key: value})
        inst_dict.update({'__class__': type(self).__name__})
        inst_dict.update({'created_at': isocre, 'updated_at': isoupd})
        return inst_dict

    def save(self):
        self.updated_at = datetime.now()