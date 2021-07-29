:tocdepth: 3

Getting Started
===============

Install
-------

Piuma is on PyPi and can be installed with PyPi::

	$ pip install piuma

Piuma can also be installed by cloning the Github_ repository and using::

	$ pip install . 

Basic Usage
-----------

Piuma is incredibly simple to install and setup requiring no external servers or dependencies. You can create a Piuma object and insert a document like so

>>> from piuma import Piuma
>>> db = Piuma()
>>> db.insert({"name": "Che Guevara", "age": 39}) 
>>> db.all()
{1: {'name': 'Che Guevara', 'age': 39}}

.. _Github: https://github.com/emit07/piuma