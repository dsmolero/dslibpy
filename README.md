
[dslibpy v0.14](https://github.com/dsmolero/dslibpy)
========================================================


DARWINIAN SOFTWARE LIBRARY FOR PYTHON
-------------------------------------
Author: [Darwin Molero](http://blog.darwiniansoftware.com/about)


Description
-----------
Contains Django/Python reusable codes. Developed by Darwin Molero, a Web
Developer.

Visit [DarwinianSoftware](http://blog.darwiniansoftware.com) for more of his
articles.


Requirements
------------
* python 2.7 (2.7.16 as of this writing)
* django >= 1.11 (1.11.23 as of this writing)


Installation
------------
You can download the tar ball from [GitHub]
(https://github.com/dsmolero/dslibpy/releases).

### Using pip

    $ pip install dslibpy-v.v.v.v.tar.gz

where v.v.v.v is the version number.

### Using setup_tools
Extract the tar ball:

    $ tar -xzf dslibpy-v.v.v.v.tar.gz

Then install:

    $ cd dslibpy
    $ python setup.py install


Modules
-------

### dslibpy.models
Reusable abstract models.

_**Entity**_

An abstract base class with the following fields:

    class Entity(models.Model):
        created_by = models.ForeignKey(get_user_model(), related_name="created_set")
        modified_by = models.ForeignKey(get_user_model(), related_name="modified_set")
        date_created = models.DateTimeField(auto_now_add=True)
        last_modified = models.DateTimeField(auto_now=True)

Pass the `user` when instantiating in subclasses. For example:

    from dslibpy.models import Entity
    
    # models.py
    class MyEntity(Entity)
        pass

    # views.py
    def myview(request):            
        myentity = MyEntity(user=request.user)


### dslibpy.forms

_**class CreditCardExpirationField**_

A field class for Credit Card expiry fields. It is of type `datetime.date`.
This field is used in conjunction with `MonthYearWidget`.

For example:

    from django import forms
    from dslibpy.forms import CreditCardExpirationField, MonthYearWidget 

    # forms.py
    class CCForm(forms.Form):
        card_expiry = CreditCardExpirationField(widget=MonthYearWidget)

    # views.py
    def index(request):
        form = CCForm(request.POST or None, initial={'card_expiry': date(2020, 2, 3)})
    
> The `day` part of the field is always the last day of the month.


### dslibpy.views

_**LoginRequiredView**_

A generic view that requires authentication on dispatch. This is a subclass of `django.views.generic.View`.
You can subclass this view and throw in some other mixins. 
    
For example:

    from dslibpy.views import LoginRequiredView
    
    class MySecretView(LoginRequiredView):
        
        def get(self, request):
            pass
    
To test, run the test web app (see below) and visit:
 
    http://localhost:8000/testloginrequired/

The browser should redirect you to:

    http://localhost:8000/accounts/login/?next=/testloginrequired/


### dslibpy.logs

Boilerplate functions for logging settings.

in settings.py:

    from dslibpy.logs import base_logging

    LOGGING = base_logging('myappname')

The `LOGGING` setting is now a dictionary that contains basic logging formatters, filters and handlers.
You will still have to update this dictionary to set the `loggers`, or you can use the presets below.

_**dev_logging**_

    dev_logging(app_name)

Logging to the console for use during development:

    from dslibpy.logs import dev_logging

    LOGGING = dev_logging('myappname')


_**pro_logging**_

    pro_logging(app_name, log_dir)
    
Logging settings for production environments. DEBUG must be False in settings.
The default log directory is `/var/tmp`

For example:

    from dslibpy.logs import pro_logging

    LOGGING = pro_logging('myappname', '/var/www/logs')

The above setting will create the log files:
 
    /var/www/logs/myappname.log
    /var/www/logs/myappname_dba.log

to check your logging configuration:

    $ python manage.py shell
    >>> from django.conf import settings
    >>> settings.LOGGING

To test, run the test web app (see below) and visit:
 
    http://localhost:8000/testlog/

The log file at `/var/tmp/tests.log` should contain the test error messages. 



### dslibpy.templatetags
Reusable template tags for formatting numbers and dates in templates. Documentation
found in [dslibpy/templatetags/README.md](dslibpy/templatetags/README.md).


Testing
-------

To run tests on `dslibpy`

    $ pipenv run python manage.py test dslibpy


Test Web App
------------

The `tests` directory inside this project's directory is a Django web application.
It is a simple app to test the features of `dslibpy`. You can launch it with:

    $ cd tests
    $ pipenv run python manage.py runserver
    
Visit `http://localhost:8000/` to see a test form in action.

