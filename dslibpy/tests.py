#!/usr/bin/env python
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

__author__ = "Darwin Molero (http://darwiniansoftware.com)"

import datetime

from django.test import TestCase
from django.utils import timezone

from templatetags import number_tags, date_tags


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class NumlibTest(TestCase):

    def test_currency(self):
        KNOWN_VALUES = (
            (0, ""),
            (0.44, "$0.44"),
            (-0.44, "-$0.44"),
            (0.4, "$0.40"),
            (-0.4, "-$0.40"),
            (1, "$1.00"),
            (-1, "-$1.00"),
            (1.04, "$1.04"),
            (-1.04, "-$1.04"),
            (1500, "$1,500.00"),
            (-1500, "-$1,500.00"),
            (11628.014, "$11,628.01"),
        )
        for input, output in KNOWN_VALUES:
            self.assertEqual(number_tags.currency(input), output)

    def test_deccomma(self):
        KNOWN_VALUES = (
            (0.44, "0.44", "0.4400"),
            (0, "", ""),
            (-0.44, "-0.44", "-0.4400"),
            (1500, "1,500.00", "1,500.0000"),
            (-1500, "-1,500.00", "-1,500.0000"),
            (11628.0123, "11,628.01", "11,628.0123"),
            (-23725.3210, "-23,725.32", "-23,725.3210"),
            (1.56789, "1.57", "1.5679"),
        )
        for n, decimal2, decimal4 in KNOWN_VALUES:
            result2 = number_tags.deccomma(n, 2)
            result4 = number_tags.deccomma(n, 4)
            self.assertEqual(decimal2, result2)
            self.assertEqual(decimal4, result4)


class TemplatetagsTest(TestCase):
    base_day = datetime.datetime(1980, 1, 1, 8, 00, 00)
    KNOWN_VALUES = (
        (datetime.datetime(2016, 3, 28, 17, 23, 00), "36 years, 2 months"),
    )

    def test_shorten_datetime(self):
        # Test same date
        today = timezone.now()
        self.assertEqual(today.time(), date_tags.shorten_datetime(today))

        # Test not same date
        delta = datetime.timedelta(days=1)
        yesterday = today - delta
        self.assertEqual(yesterday.date(), date_tags.shorten_datetime(yesterday))

    def test_timediff(self):
        for someday, result in self.KNOWN_VALUES:
            ret = date_tags.timediff(self.base_day, someday)
            self.assertEqual(ret, result)
