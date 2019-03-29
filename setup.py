#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

PACKAGE_NAME = 'fluffycow'
VERSION = '0.0.5'


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    python_requires='>=3.5',
    description='A domain-specific language for generating random inputs',
    long_description=open('README.rst').read(),
    author='Chris Timperley',
    author_email='ctimperley@cmu.edu',
    url='https://github.com/ChrisTimperley/fluffycow',
    license='Apache License 2.0',
    install_requires=['typing-extensions>=3.7.2'],
    packages=['fluffycow'],
    keywords=['random', 'fuzzing', 'dsl'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
