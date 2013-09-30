__author__ = "Darwin Molero"


from django.contrib.humanize.templatetags.humanize import intcomma
from django.template import Library
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from apps.dslibpy.numbers import format_currency

register = Library()

#-------------------------------------------------------------------------------
@register.filter
def currency(amount, decimals=4):
    return format_currency(amount, decimals)

#-------------------------------------------------------------------------------
@register.filter
def colored_currency(amount):
    """
    Format numbers with commas and 2 decimal places.
    """
    amt_str = format_currency(amount, 2)
    class_str = _get_class_str(amount)
    html = '<span class="{0}">{1}</span>'.format(class_str, amt_str)
    return mark_safe(html)


#-------------------------------------------------------------------------------
@register.filter
def colored_percent(amount):
    """
    Format percent values with 2 decimal places and the percent sign.
    """
    if not amount or isinstance(amount, str):
        return "-"
    percent_str = format_currency(amount, 2)
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
