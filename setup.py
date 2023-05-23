# setup.py

from setuptools import setup, Extension

setup(
    name='my_library',
    version='1.0',
    author='Your Name',
    description='A simple C library for Python',
    ext_modules=[Extension('my_library', sources=['my_library.c'])]
)
