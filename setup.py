#!/usr/bin/env python
from setuptools import setup, find_packages

requires = [
       'django',
        'channels'
       ]

setup(name='meu_site',
     version='1.0',
     packages=find_packages(),
     install_requires=requires)