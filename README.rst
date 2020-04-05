# rwalang (detect ikinyarwanda)
=======================
A fast language detection package for Ikinyarwanda(Native language of Rwandans)

⚠ Be aware that if a sentence has foreign language mixed with Ikinyarwanda rwalang returns `false`

Installation
------------

The distribution is hosted on pypi at: https://pypi.org/project/rwalang/. To directly install the package from pypi, run from your terminal::

    $ pip install rwalang

Usage
----------- 

Detect Ikinyarwanda
=========================

.. code-block :: python

   from rwalang import isKinyarwanda

   print(isKinyarwanda("Thank you!")); //false
   print(isKinyarwanda("Murakoze!")); //true
   print(isKinyarwanda("Mu myandikire ya gihaânga")); //true
   print(isKinyarwanda("Iminsi n'imitindi")); //true
   print(isKinyarwanda("Yangurije amafaranga magana atanu")); //true
   print(isKinyarwanda("mbega i nigga")); //false 😂
