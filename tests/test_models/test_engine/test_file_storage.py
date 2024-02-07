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

    def test_save_reload(self):
        test_store = models.engine.file_storage.FileStorage()
        test_object = models.base_model.BaseModel()
        test_store._FileStorage__file_path = "test_store.json"
        test_store.save()
        alt_object = models.base_model.BaseModel()
        with open(test_store._FileStorage__file_path, 'r') as file:
            presave = json.load(file)
        test_store.save()

        with open(test_store._FileStorage__file_path, 'r') as file:
            postsave = json.load(file)
        self.assertNotEqual(presave, postsave)
        alt_store = models.engine.file_storage.FileStorage()
        alt_store._FileStorage__objects = {}
        alt_store._FileStorage__file_path = "test_store.json"
        self.assertEqual(alt_store.all(), {})
        alt_store.reload()
        self.assertNotEqual(alt_store.all(), {})

