# -*- coding: utf-8 -*-

from unittest import TestCase

from functions import swap_last_to_first

class TestSwapLastToFist(TestCase):
    def test_must_swap_last_to_first_correctly(self):
        result = swap_last_to_first('amp')
        self.assertEqual(result, 'pam')