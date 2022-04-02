from django.template import Library, Node
from django.forms.widgets import CheckboxInput, RadioSelect


register = Library()


@register.filter
def is_boolean(field):
    # return isinstance(value, CheckboxInput)
    boolean_widgets = [CheckboxInput, RadioSelect]
    try:
        widget = field.field.widget
    except AttributeError:
        widget = field.widget
    _is_boolean = type(widget) in boolean_widgets
    return _is_boolean


__author__ = 'darwin'
