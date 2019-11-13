__author__ = 'Darwin Molero (http://darwiniansoftware.com)'

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dslibpy',
    version='0.14',
    packages=[
        'dslibpy',
        'dslibpy.templatetags',
    ],
    include_package_data=True,
    #license='BSD License',  # example license
    license='LICENSE.txt',
    description='Darwinian Software Library for Python',
    long_description=README,
    url='http://darwiniansoftware.com/',
    author='Darwin Molero',
    author_email='darwinm@coderax.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License', # example license
        'License ::',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django >= 1.11",
    ]
)
