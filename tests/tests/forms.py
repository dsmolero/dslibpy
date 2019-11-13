from django import forms
from dslibpy.forms import SplitMonthYearField, SplitMonthYearWidget, CreditCardExpirationField, MonthYearWidget


class MonthYearForm(forms.Form):

    month_year = SplitMonthYearField(widget=SplitMonthYearWidget(required=False), required=False,
                                     help_text='SplitMonthYearField')
    vacation = SplitMonthYearField('SplitMonthYearField *', widget=SplitMonthYearWidget(),
                                   help_text='SplitMonthYearField (required)')
    expiry_date = CreditCardExpirationField(help_text='CreditCardExpirationField (date)')
    card_expiry = CreditCardExpirationField(widget=MonthYearWidget,
                                            help_text='CreditCardExpirationField using MonthYearWidget')
