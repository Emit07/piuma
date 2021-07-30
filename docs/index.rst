.. piuma documentation master file, created by
   sphinx-quickstart on Wed Jul 28 15:28:18 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Piuma!
=================

An ultra-lighweight document oriented database in external dependancy free python.

>>> from piuma import Piuma
>>> db = Piuma()
>>> db.insert({"name": "Che Guevara", "age": 39}) 
>>> db.all()
{1: {'name': 'Che Guevara', 'age': 39}}

Quick Links
-----------
- Github: https://github.com/emit07/piuma
- Documentation: https://piuma.readthedocs.io/
- PyPi: https://pypi.org/project/piuma

Table of Contents
-----------------
.. toctree::
   :maxdepth: 2
   
   readme
   getting-started
   usage

Other
-----


* :ref:`search`
