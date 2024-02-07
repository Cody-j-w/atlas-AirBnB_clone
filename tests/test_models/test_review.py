#!/usr/bin/python3

import unittest
import models


class TestReviewAttributes(unittest.TestCase):
    def test_review_init(self):
        review = models.review.Review()
        self.assertIsInstance(review, models.review.Review)
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attributes(self):
        review = models.review.Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")