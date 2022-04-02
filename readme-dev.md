dslibpy/readme-dev.md
=====================


Testing
-------
at the project directory

    $ python setup.py pytest
    

Versioning convention
---------------------
    <rewrite>.<new feature>.<bug-fix>.<doc-ui-change>


New Releases
------------
    
1. Update the dependency requirements in setup.py    
    - packages
    - install_requires
    - setup_requires
    - tests_require
    - setup(classifiers=['Programming Language :: Python' ...] ...)

2. Change the version number in the first line of README.md

3. Change the version number in setup.py
    - setup(version='v.v.v.v' ...)
    
4. Update the CHANGELOG.md


Recompiling
-----------
at the project directory
    
    $ python setup.py sdist
