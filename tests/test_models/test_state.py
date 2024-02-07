#!/usr/bin/python3

import unittest
import models


class TestStateAttributes(unittest.TestCase):
    def test_state_init(self):
        state = models.state.State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_state_name(self):
        state = models.state.State()
        state.name = "Oklahoma"

        self.assertNotEqual(state.name, "OK")
