from logging import getLogger
from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse

from dslibpy.views import LoginRequiredView
from .forms import MonthYearForm


log = getLogger(__name__)

def index(request):
    template_name = 'base.html'
    form = MonthYearForm(request.POST or None, initial={'card_expiry': date(2020, 2, 3)})
    context = {
        'form': form
    }
    if request.method == 'POST':
        if form.is_valid():
            context.update({
                'month_year': form.cleaned_data['month_year'],
                'data_type': type(form.cleaned_data['month_year']).__name__,
                'vacation': form.cleaned_data['vacation'],
                'expiry_date': form.cleaned_data['expiry_date'],
                'card_expiry': form.cleaned_data['card_expiry'],
            })
    return render(request, template_name, context)


class TestLoginRequiredView(LoginRequiredView):

    def get(self, request):
        return HttpResponse('You have reached a view that requires authentication.')


def test_log(request):
    log.debug('This is a test debug message.')
    log.error('This is a test error message.')
    return HttpResponse('logged test messages to /var/tmp/tests.log')
