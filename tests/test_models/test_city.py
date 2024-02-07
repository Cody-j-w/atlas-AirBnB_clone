#!/usr/bin/python3

import unittest
import models


class TestCityAttributes(unittest.TestCase):
    def test_city_init(self):
        city = models.city.City()
        self.assertIsInstance(city, models.city.City)
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_attributes(self):
        city = models.city.City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
