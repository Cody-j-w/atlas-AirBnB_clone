#!/usr/bin/python3

import unittest
import time
from datetime import datetime
from models.base_model import BaseModel

class TestBaseMethods(unittest.TestCase):
    def test_save_method(self):
        b1 = BaseModel()
        update_1 = b1.updated_at
        time.sleep(0.001)
        b1.save()
        update_2 = b1.updated_at
        self.assertNotEqual(update_1, update_2)

    def test_to_dict_method(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertEqual(b1_dict, b1.to_dict())

    def test_base_attributes(self):
        b1 = BaseModel()
        s = "[{0}] ({1}) {2}".format(type(b1).__name__, b1.id, b1.__dict__)
        self.assertEqual(b1.__str__(), s)

    def test_created_at(self):
        b1 = BaseModel()
        self.assertEqual(b1.created_at, datetime.now())
