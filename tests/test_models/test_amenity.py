#!/usr/bin/python3

import unittest
import models


class TestStateAttributes(unittest.TestCase):
    def test_amenity_init(self):
        amenity = models.amenity.Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_attributes(self):
        amenity = models.amenity.Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")