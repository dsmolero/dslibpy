#!/usr/bin/env python
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

__author__ = "Darwin Molero (http://darwiniansoftware.com)"

import unittest

from numlib import deccomma


class SimpleTest(unittest.TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class NumbersTest(unittest.TestCase):

    KNOWN_VALUES = (
        (0.44, "0.4400"),
        (0, ""),
        (-0.44, "-0.4400"),
        (1500, "1,500.0000"),
        (-1500, "-1,500.0000"),
        (11628.0123, "11,628.0123"),
        (-23725.3210, "-23,725.3210"),
        (1.56789, "1.5679"),
    )

    def test_num_to_string(self):
        for n, s in self.KNOWN_VALUES:
            result = deccomma(n)
            self.assertEqual(s, result)


if __name__ == '__main__':
    unittest.main()
