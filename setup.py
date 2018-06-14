#!/usr/bin/env python

from setuptools import setup

setup(name='visdomino',
      version='0.1.0',
      description='Visdomino sends files to Visdom.',
      author='Larry Neal',
      author_email='nealla@lwneal.com',
      scripts=['scripts/visdomino'],
      install_requires=[
          "visdom",
      ],
)
