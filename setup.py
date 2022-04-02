__author__ = 'Darwin Molero (http://darwiniansoftware.com)'

import os
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

#
# packages in this project
#
packages = [
    'dslibpy',
    'dslibpy/templatetags',
    ]

#
# Required packages when deployed by end users in production
#
install_requires = [
    'Django>=2.2,<2.3',
    ]

#
# Dependencies for development
#
setup_requires = [
    'pytest<7,>=5',
    'pytest-django',
    'pytest-factoryboy',
    'pytest-runner',
    'wheel',
    'setuptools',
    ]

#
# Dependencies for running tests in development
#
tests_require = [
    ]

setup(
    name='dslibpy',
    version='3.7.2-2.2',
    author='Darwin Molero',
    author_email='darwinm@coderax.com',
    url='http://darwiniansoftware.com/',
    packages=packages,
    python_requires='>=3.7',
    include_package_data=True,
    #license='BSD License',  # example license
    license='LICENSE.txt',
    description='Darwinian Software Library for Python',
    long_description=README,
    classifiers=[
        'Environment :: Web Environment',
        # specify the Django version in the install_requires list above
        'Framework :: Django',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License', # example license
        'License ::',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
