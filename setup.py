#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rwalang",
    version='0.0.5',
    url="https://github.com/knowbee/pyrwalang.git",
    description="A fast language detection package for Ikinyarwanda(Native language of Rwandans)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["rwalang"],
    packages=find_packages(),
    keywords=["detect language",
              "rwanda",
              "ikinyarwanda",
              "u rwanda"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
    ],
    author='Igwaneza Bruce',
    author_email='knowbeeinc@gmail.com',
    license='MIT',
    zip_safe=False,

)
