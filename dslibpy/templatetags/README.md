dslibpy.templatetags
====================
Darwinian Software Library for Python

    Author: [Darwin Molero](http://blog.darwiniansoftware.com/about)

number_tags
-----------

_**currency**_

Use system locale settings to format currency numbers.


_**deccomma**_

Humanize a number in the standard form -99,999.99


date_tags
---------

_**shorten_datetime**_

Given a datetime as *dt*:
return only the time part of *dt* if *dt* is today,
otherwise, return only the date part of it.


form_tags
---------

_**is_boolean**_

Given a form field as `field`:
return if the field is a checkbox or a radio button.

ex:

    # _form.html
    {% load widget_tweaks %}
    {% load form_tags %}
    {% for field in form.visible_fields %}
    {% if field|is_boolean %}
    {{ field }}
    {% else %}
    {{ field|add_class:"w-75" }}
    {% endif %}
    {% endfor %}


<< [Back to Main](../../README.md)
