#!/usr/bin/env python
# django-userskins -  support for skins in django

"""Skins support for django

A django app that allows for skins support
"""

from distutils.core import setup


description, long_description = __doc__.split('\n\n', 1)
VERSION = '0.1'

setup(
    name='django-userskins',
    version=VERSION,
    author='Goldan',
    author_email='denis.golomazov@gmail.com',
    description=description,
    long_description=long_description,
    license='GPL',
    platforms=['any'],
    url='http://github.com/Goldan/django-userskins/',
    packages=['userskins'],
    requires=['django (>=1.1)'],
    )
