#!/usr/bin/python3

import unittest
import time
import json
from datetime import datetime
import models
from ...test_models import test_storage

class TestFileStorageMethods(unittest.TestCase):
    def test_file_path(self):
        self.assertEqual(test_storage._FileStorage__file_path, "storage.json")

    def test_object_dict(self):
        self.assertEqual(type(test_storage._FileStorage__objects), dict)

    def test_all_method(self):
        self.assertEqual(test_storage.all(), test_storage._FileStorage__objects)


    def test_new_method(self):
        b1 = models.base_model.BaseModel()
        key = "{0}.{1}".format(type(b1).__name__, b1.id)
        self.assertEqual(b1, test_storage._FileStorage__objects[key])

    def test_save_and_reload_method(self):
        test_dict = test_storage._FileStorage__objects
        test_storage.save()

        test_storage.reload()
        self.assertEqual(test_dict, test_storage._FileStorage__objects)
        