__author__ = "Darwin Molero (http://darwiniansoftware.com)"


import datetime
from django.template import Library

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
    present = datetime.datetime.now()

    if dt.date() == present.date():
        return dt.time()
    else:
        return dt.date()
