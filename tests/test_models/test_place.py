#!/usr/bin/python3

import unittest
import models


class TestPlaceAttributes(unittest.TestCase):
    def test_place_init(self):
        test_place = models.place.Place()
        self.assertIsInstance(test_place, models.place.Place)
        self.assertTrue(hasattr(test_place, "city_id"))
        self.assertTrue(hasattr(test_place, "user_id"))
        self.assertTrue(hasattr(test_place, "name"))
        self.assertTrue(hasattr(test_place, "description"))

    def test_variable_attributes(self):
        test_place = models.place.Place()
        self.assertEqual(test_place.city_id, "")
        self.assertEqual(test_place.user_id, "")
        self.assertEqual(test_place.name, "")
        self.assertEqual(test_place.description, "")
        self.assertEqual(test_place.number_rooms, 0)
        self.assertEqual(test_place.number_bathrooms, 0)
        self.assertEqual(test_place.max_guest, 0)
        self.assertEqual(test_place.price_by_night, 0)
        self.assertEqual(test_place.latitude, 0.0)
        self.assertEqual(test_place.longitude, 0.0)
