# rwalang (detect ikinyarwanda)
=================================
.. image:: https://travis-ci.com/knowbee/pyrwalang.svg?token=yN9jXnk59suszMqNsJJb&branch=master
    :target: https://travis-ci.com/knowbee/pyrwalang
.. image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=102
    :target: https://github.com/ellerbrock/open-source-badge/

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
