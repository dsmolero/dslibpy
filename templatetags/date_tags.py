__author__ = "Darwin Molero"


import datetime
#from datetime import datetime
from django.template import Library
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = Library()

#-------------------------------------------------------------------------------
@register.filter
def colored_date(date, date_format="%b-%d-%Y", time_format="%I:%M%p"):
    """
    Return a red colored or green colored date.
    Green when the last updated price is the most recent price of the stock.
    Otherwise, it should be red.
    The most recent price should be the price of the stock at the last market
    close.
    """
    present = datetime.datetime.now()
    # cut-off is today's close
    cut_off_time = datetime.time(hour=15, minute=30)
    cut_off = datetime.datetime.combine(present.date(), cut_off_time)
    if present < cut_off:
        # current time is before market close, set cut-off to yesterday's close
        td = datetime.timedelta(days=1)
        cut_off -= td
    if cut_off.weekday() > 4:
        # it's a weekend, move cut-off to the last business day (friday)
        subtract = cut_off.weekday() - 4
        td = datetime.timedelta(days=subtract)
        cut_off -= td

    if date > cut_off:
        class_str = "positive"
    else:
        class_str = "negative"
    date_str = date.strftime(date_format)
    time_str = date.strftime(time_format).lower()
    ret = '<span class="{0}">{1} {2}</span>'.format(class_str, date_str, time_str)
    return mark_safe(ret)