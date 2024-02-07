#!/usr/bin/python3

import unittest
import time
from datetime import datetime
from models.user import User

class TestUserAttributes(unittest.TestCase):
    def test_user_attrs(self):
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

    def test_user_values(self):
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

if __name__ == '__main__':
    unittest.main()
