from django.template import Library, Node
from django.forms.widgets import CheckboxInput, RadioSelect


register = Library()


@register.filter
def is_boolean(field):
    # return isinstance(value, CheckboxInput)
    boolean_widgets = [CheckboxInput, RadioSelect]
    widget = field.field.widget
    _is_boolean = type(widget) in boolean_widgets
    print(type(widget), _is_boolean)
    return _is_boolean


__author__ = 'darwin'