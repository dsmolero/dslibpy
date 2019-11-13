__author__ = "Darwin Molero (http://darwiniansoftware.com)"

from unicodedata import normalize

from datetime import datetime
from django.template import Library
from django.utils import timesince


register = Library()


@register.filter
def shorten_datetime(dt):
    """
    Given a datetime as dt:
    return only the time part of dt if dt is today,
    otherwise, return only the date part of dt.
    :param dt:
    :return datetime:
    """
    present = datetime.now()

    if dt.date() == present.date():
        return dt.time()
    else:
        return dt.date()


@register.filter
def timediff(value, arg=None):
    """
    Timedelta tag will humanize output correctly for both future and past dates using now as a default
    reference date (or a specified reference date as argument)
    """
    if not value:
        return ''
    if arg:
        cmp = arg
    else:
        cmp = datetime.now()
    if arg:
        return normalize('NFKD', timesince.timesince(value,cmp))
    elif value > cmp:
        return "in %s" % timesince.timesince(cmp,value)
    else:
        return "%s ago" % timesince.timesince(value,cmp)
