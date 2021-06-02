dslibpy/CHANGELOG.md
====================

CHANGE LOG
----------
##### Darwinian Software Library for Python
Author: [Darwin Molero](http://blog.darwiniansoftware.com/about)


v3.7.22
-------
This release is not backwards compatible with earlier versions.

Changes:
- first version to support Python 3
- version number meanings:
    v3  => support for Python 3
    .7  => supports Python 3.7
    .22 => support for Django 2.2
    .0  => bugfix
- Bumped for Django 2.2 and Python 3.7
- Now using setuptools configurations
- Now using pytest test runner


v0.14
-----
This release is not backwards compatible with earlier versions.

Now using pipenv.
Bumped requirement to Django 1.11

Added:

* class models.Entity
* class forms.CreditCardExpirationField
* class forms.MonthYearWidget
* class forms.SplitMonthYearField
* class forms.SplitMonthYearWidget
* class views.LoginRequiredView
* logs.base_logging()
* logs.pro_logging()
* logs.dev_logging()
* utils.insert_before()
* utils.remove_non_ascii_1()
* utils.str2bool()
* utils.eprint()


v0.12
-----
This release is not backwards compatible with earlier versions.

Removed the numlib module.

Removed the views module. Any of the following packages are superior for the same purpose:

* [django-permission](http://django-permission.readthedocs.org/en/latest/)
* [django-object-permissions](https://pypi.python.org/pypi/django-object-permissions)
* [django-guardian](https://pythonhosted.org/django-guardian/userguide/check.html)

The *decimals* parameter for *templatetags.number_tags.deccomma* now defaults to 2.

Tested to work in Django 1.9


v0.11.1
-------
This release is not backwards compatible with earlier versions.

Removed template tag colored_date as it is specific to a particular application and not as a generic library.

Added documentation for date_tags.shorten_datetime template tag.


v0.11
-----
Added template tag date_tags


v0.10.1.0
---------
This release is not backwards compatible with earlier versions.

Renamed dslibpy.numbers to dslibpy.numlib to avoid collision with python's numbers package.

Fixed a bug in dslibpy.numlib.deccomma that removes the sign when converting negative fractions between -1 and 0.

Added the tests project to build test suites for dslibpy .


v0.10.0.2
---------
Fixed bugs in README.md documentation examples.


v0.10.0.1
---------
Lowered the requirement to Django 1.2

Fixed grammar errors in the documentation.


v0.10.0.0
---------
Packaged dslibpy into a Python redistributable.

Changed dslibpy.numbers.currency 
	to dslibpy.numbers.deccomma

Changed dslibpy.numbers.colored_currency
	to dslibpy.numbers.deccomma_color_html

Changed dslibpy.numbers.colored_percent
	to dslibpy.numbers.percent_color_html

Added documentation for dslibpy.numbers

Added documentation for dslibpy.templatetags 
