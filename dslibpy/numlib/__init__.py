__author__ = 'Darwin Molero (http://darwiniansoftware.com)'

from django.contrib.humanize.templatetags.humanize import intcomma


def deccomma(amount, decimals=4):
    """
    Format numbers with commas and 4 decimal places.
    """
    if not amount or isinstance(amount, str):
        return ""
    decimal_part = intcomma("%0.{0}f".format(decimals) % amount)
    return decimal_part
