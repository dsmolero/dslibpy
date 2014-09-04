__author__ = "Darwin Molero (http://darwiniansoftware.com)"


from django.template import Library
# from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from dslibpy import numlib

register = Library()

#-------------------------------------------------------------------------------
@register.filter
def deccomma(amount, decimals=4):
    return numlib.deccomma(amount, decimals)

#-------------------------------------------------------------------------------
@register.filter
def deccomma_color_html(amount):
    """
    Format numbers with commas and 2 decimal places.
    """
    amt_str = numlib.deccomma(amount, 2)
    class_str = _get_class_str(amount)
    html = '<span class="{0}">{1}</span>'.format(class_str, amt_str)
    return mark_safe(html)


#-------------------------------------------------------------------------------
@register.filter
def percent_color_html(amount):
    """
    Format percent values with 2 decimal places and the percent sign.
    """
    if not amount or isinstance(amount, str):
        return "-"
    percent_str = numlib.deccomma(amount, 2)
    class_str = _get_class_str(amount)
    html = '<span class="{0}">{1}%</span>'.format(class_str, percent_str)
    return mark_safe(html)


#-------------------------------------------------------------------------------
def _get_class_str(amount):
    if amount > 0:
        class_str = "positive"
    elif amount < 0:
        class_str = "negative"
    else:
        class_str = "zero"
    return class_str
