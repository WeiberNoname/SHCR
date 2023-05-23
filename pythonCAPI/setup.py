# setup.py

from setuptools import setup, Extension

setup(
    name='library',
    version='1.0',
    author='Your Name',
    description='A simple C library for Python',
    ext_modules=[Extension('library', sources=['library.c'])]
)

