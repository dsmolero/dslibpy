__author__ = "Darwin Molero (http://darwiniansoftware.com)"

from calendar import monthrange, month_name
from datetime import date, datetime
from django import forms
from django.core.validators import MinValueValidator
from django.forms.fields import EMPTY_VALUES
from django.utils.translation import ugettext as _
from logging import getLogger


log = getLogger(__name__)


class CreditCardExpirationField(forms.DateField):
    default_error_messages = {
        'min_value': _("This card has expired."),
        'invalid': _("Please specify a valid expiration date.")
    }
    default_validators = [
        MinValueValidator(date.today()),
    ]
    input_formats = ('%m/%Y', '%m/%y')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', forms.DateInput(format='%m/%Y'))
        super(CreditCardExpirationField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """
        Set day to last day of month.
        Credit cards are valid through the last day of the specified month.
        """
        value = super(CreditCardExpirationField, self).to_python(value)
        if isinstance(value, list):
            month = value[0]
            year = value[1]
        else:
            month = value.month
            year = value.year
        last_day = monthrange(year, month)[1]
        card_expiry = date(year, month, last_day)
        log.debug('ret: {}'.format(card_expiry))
        return card_expiry


class MonthYearWidget(forms.MultiWidget):
    MONTHS = {ii: ss[:3] for ii, ss in enumerate(month_name)}

    def __init__(self, attrs=None, min_year=None, max_year=None, required=True):
        year_now = date.today().year
        if not min_year:
            min_year = year_now
        if not max_year:
            max_year = year_now + 10
        year_choices = [(year, year) for year in range(min_year, max_year + 1)]
        month_choices = [(month, abbr) for month, abbr in self.MONTHS.items()]
        if not required:
            year_choices.append((None, '----'))
            year_choices.sort()
            month_choices[0] = (None, '---')
        else:
            del(month_choices[0])
        widgets = (forms.Select(choices=month_choices, attrs=attrs), forms.Select(choices=year_choices, attrs=attrs))
        super(MonthYearWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.month, value.year]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % ii)
            for ii, widget in enumerate(self.widgets)
        ]
        try:
            month = int(datelist[0])
            year = int(datelist[1])
            d = date(day=monthrange(year, month)[1], month=month, year=year)
        except ValueError:
            return None
        else:
            return d


class SplitMonthYearField(forms.MultiValueField):
    default_error_messages = {
        'invalid_month': _(u'Enter a valid month.'),
        'invalid_year': _(u'Enter a valid year.'),
    }

    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            forms.IntegerField(error_messages={'invalid': errors['invalid_month']}),
            forms.IntegerField(error_messages={'invalid': errors['invalid_year']}),

        )
        super(SplitMonthYearField, self).__init__(fields, *args, **kwargs)

    def compress(self, value_list):
        if value_list:
            if value_list[0] in EMPTY_VALUES:
                raise forms.ValidationError(self.error_messages['required'])
            if value_list[1] in EMPTY_VALUES:
                raise forms.ValidationError(self.error_messages['required'])
            return value_list
        return None


class SplitMonthYearWidget(forms.MultiWidget):
    MONTHS = {ii: ss[:3] for ii, ss in enumerate(month_name)}

    def __init__(self, attrs=None, min_year=None, max_year=None, required=True):
        year_now = date.today().year
        if not min_year:
            min_year = year_now
        if not max_year:
            max_year = year_now + 10
        year_choices = [(year, year) for year in range(min_year, max_year + 1)]
        month_choices = [(month, abbr) for month, abbr in self.MONTHS.items()]
        if not required:
            year_choices.append((None, '----'))
            year_choices.sort()
            month_choices[0] = (None, '---')
        else:
            del(month_choices[0])
        widgets = (forms.Select(choices=month_choices, attrs=attrs), forms.Select(choices=year_choices, attrs=attrs))
        super(SplitMonthYearWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value[0], value[1]]
        return [None, None]
