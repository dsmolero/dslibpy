dslibpy/readme-dev.md
=====================


Testing
-------
at the project directory

    $ cd tests
    $ python manage.py test dslibpy
    

Versioning convention
---------------------
    <rewrite>.<new feature>.<bug-fix>.<doc-ui-change>


New Releases
------------
    1. Change the version number in the first line of README.md
    2. Change the version number in setup.py
    3. Update the CHANGELOG.md


Recompiling
-----------
at the project directory
    
    $ python setup.py sdist
