#!/usr/bin/env python
from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rwalang",
    version='0.0.4',
    description="A fast language detection package for Ikinyarwanda(Native language of Rwandans)",
    long_description=long_description,
    py_modules=["rwalang"],
    package_dir={'.': 'rwalang'},
    keywords=["detect language",
              "rwanda",
              "ikinyarwanda",
              "u rwanda"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: MIT :: MIT License",
            "Operating System :: OS Independent",
    ],
    author='Igwaneza Bruce',
    author_email='knowbeeinc@gmail.com',
    license='MIT',
    zip_safe=False,

)
