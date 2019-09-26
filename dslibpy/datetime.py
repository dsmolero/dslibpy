import  pytz

from datetime import datetime
from dateutil.relativedelta import relativedelta


def in_n_minutes(minutes):
    """
    Return the datetime n minutes from now. For convenience
    The returned datetime is timezone aware.
    """
    return datetime.utcnow().replace(tzinfo=pytz.utc) + relativedelta(minutes=minutes)
