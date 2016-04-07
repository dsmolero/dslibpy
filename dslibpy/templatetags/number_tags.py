__author__ = "Darwin Molero (http://darwiniansoftware.com)"


import locale

from django.contrib.humanize.templatetags.humanize import intcomma
from django.template import Library
from django.template.defaultfilters import floatformat
# from django.utils.html import conditional_escape


register = Library()


@register.filter()
def currency(value):
    """
    Use system locale settings to format currency numbers.
    """
    if not value:
        return ""
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(value, grouping=True)


@register.filter
def deccomma(amount, decimals=2):
    """
    Humanize a number in the standard form -99,999.99
    """
    if not amount:
        return ""
    return intcomma(floatformat(amount, decimals))
