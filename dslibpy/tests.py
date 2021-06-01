#!/usr/bin/env python
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

__author__ = "Darwin Molero (http://darwiniansoftware.com)"

from django import forms
from django.test import TestCase
from datetime import datetime, timedelta, date

from .templatetags import number_tags, date_tags, form_tags
from .forms import CreditCardExpirationField, MonthYearWidget
from .utils import eprint


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
    base_day = datetime(1980, 1, 1, 8, 00, 00)
    KNOWN_VALUES = (
        (datetime(2016, 3, 8, 17, 23, 00), "36 years, 2 months"),
    )

    def test_shorten_datetime(self):
        # Test same date
        today = datetime.today()
        self.assertEqual(today.time(), date_tags.shorten_datetime(today))

        # Test not same date
        delta = timedelta(days=1)
        yesterday = today - delta
        self.assertEqual(yesterday.date(), date_tags.shorten_datetime(yesterday))

    def test_timediff(self):
        for someday, result in self.KNOWN_VALUES:
            ret = date_tags.timediff(self.base_day, someday)
            self.assertEqual(ret, result)

    def test_is_boolean(self):

        class F(forms.Form):
            member_name = forms.CharField(max_length=255)
            is_active = forms.BooleanField()

        f = F()
        self.assertTrue(form_tags.is_boolean(f.fields['is_active']))
        self.assertFalse(form_tags.is_boolean(f.fields['member_name']))


class UtilsTest(TestCase):

    def test(self):
        eprint('This is a test error message.')
        eprint('This is another error message.')


class CreditCardExpirationFieldTest(TestCase):

    def test(self):

        class F(forms.Form):
            cce = CreditCardExpirationField(widget=MonthYearWidget(min_year=2019, max_year=2021))

        initial = {'cce': date(2020, 2, 1)}
        f = F(initial=initial)
        expected_html = '<p><label for="id_cce_0">Cce:</label> ' \
            + '<select name="cce_0" required id="id_cce_0">' \
            + '<option value="1">Jan</option>' \
            + '<option value="2" selected>Feb</option>' \
            + '<option value="3">Mar</option>' \
            + '<option value="4">Apr</option>' \
            + '<option value="5">May</option>' \
            + '<option value="6">Jun</option>' \
            + '<option value="7">Jul</option>' \
            + '<option value="8">Aug</option>' \
            + '<option value="9">Sep</option>' \
            + '<option value="10">Oct</option>' \
            + '<option value="11">Nov</option>' \
            + '<option value="12">Dec</option>' \
            + '</select><select name="cce_1" required id="id_cce_1">' \
            + '<option value="2019">2019</option>' \
            + '<option value="2020" selected>2020</option>' \
            + '<option value="2021">2021</option>' \
            + '</select></p>'
        html = f.as_p()
        self.assertEqual(expected_html, html)

        test_input = {'cce_0': 5, 'cce_1': 2021}
        f = F(data=test_input)
        html = f.as_p()
        expected_html = '<ul class="errorlist"><li>This card has expired.</li></ul>\n' \
            + '<p><label for="id_cce_0">Cce:</label> ' \
            + '<select name="cce_0" required id="id_cce_0">' \
            + '<option value="1">Jan</option>' \
            + '<option value="2">Feb</option>' \
            + '<option value="3">Mar</option>' \
            + '<option value="4">Apr</option>' \
            + '<option value="5" selected>May</option>' \
            + '<option value="6">Jun</option>' \
            + '<option value="7">Jul</option>' \
            + '<option value="8">Aug</option>' \
            + '<option value="9">Sep</option>' \
            + '<option value="10">Oct</option>' \
            + '<option value="11">Nov</option>' \
            + '<option value="12">Dec</option>' \
            + '</select><select name="cce_1" required id="id_cce_1">' \
            + '<option value="2019">2019</option>' \
            + '<option value="2020">2020</option>' \
            + '<option value="2021" selected>2021</option>' \
            + '</select></p>'
        self.assertEqual(html, expected_html)

        test_input = {'cce_0': 8, 'cce_1': date.today().year + 1}
        f = F(data=test_input)
        valid = f.is_valid()
        self.assertTrue(valid)
