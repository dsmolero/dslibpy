__author__ = 'Darwin Molero (http://darwiniansoftware.com)'

from django.contrib.humanize.templatetags.humanize import intcomma


def deccomma(amount, decimals=4):
    """
    Format numbers with commas and 4 decimal places.
    """
    if not amount or isinstance(amount, str):
        return ""
    decimals = int(decimals)
    amount = round(float(amount), decimals)
    whole_num = intcomma(int(amount))
    decimal_part = "%0.{0}f".format(decimals) % amount
    decimal_part = decimal_part[-1 - decimals:]
    return "{0}{1}".format(whole_num, decimal_part)
