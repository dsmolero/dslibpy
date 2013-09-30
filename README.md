dslibpy
=======
Darwinian Software Python library
---------------------------------
Author: [__Darwin Molero__](http://blog.darwiniansoftware.com/about)
(this document is best viewed with a Markdown viewer.)

Description:
------------
Contains Django/Python reusable codes. Developed by Darwin Molero, a Web Developer.

Visit [__DarwinianSoftware__](http://blog.darwiniansoftware.com) for more of his articles.

Requirements:
-------------
* python 2.7+   (tested upto python 2.7.3)
* django 1.3+   (tested with django < 1.4)

Installation:
-------------
You can download the .zip file [here](https://github.com/darwinmolero/dslibpy). Extract
and place the dslibpy folder in your project root directory. So if your project is
in the folder:

    ~/django/myproject

then the folder dslibpy will be in:

    ~/django/myproject/dslibpy/

(Geek says "I will put mine in /usr/local/bin/dslibpy/ and symlink it to my project root.")

Well? ^_6

Modules:
--------

### dslibpy.views.restricted
Django class-based-views with object-level permissions checking. Documentation found in
[dslibpy/views/README.md](views/README.md)

### dslibpy.numbers
Reusable utility functions to format numbers that have decimal parts. Documentation found in
[dslibpy/numbers/README.md](numbers/README.md)

### dslibpy.templatetags
Reusable template tags for formatting numbers, dates in templates. Documentation found in
[dslibpy/templatetags/README.md](templatetags/README.md)
