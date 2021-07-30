Usage
==========

Insert
------

.. Sorry for the spaces instead of the tabs but the tabs are rendered too long on readthedocs.io (for my taste)
.. code-block:: python

	piuma.insert(
	    data: Dict,
	    id: Optional[int]=None # Generates new id if left empty
	) -> id: int

Inserts a new document into the database. The document value field only takes in dictionaries. This functions returns the value of the document once inserted.
	
.. code-block:: python

	>>> from piuma import Piuma
	>>> db = Piuma()
	>>> db.insert({"a":0})

Insert a document with a specific id with an integer value, this field is optional. 

.. code-block:: python

	>>> db.insert({"b":1}, id=1234)
	>>> db.insert({"c":[0,1,2]})

.. Note:: The automatic ids that documents without a specified id receive go from the biggest id in the database, if you insert new document with a specified id of 1234 the next document's id will be 1235 unless specified.

Get
---

.. code-block:: python

	piuma.get(
	    id: int
	) -> Document: Document

Returns a document by the id. The document id field only takes in integers.

	>>> db.get(id=1)
	{'a':0}


Remove
------

.. code-block:: python

	piuma.remove(
	    id: int
	) -> None

Removes a document by the specified id. The document id field only takes in integers.

	>>> db.remove(id=1234)


Update
------

.. code-block:: python

	piuma.update(
	    data: Dict,
	    id: int
	) -> None

Updates a document by the id. The document id field only takes in integers. This function completely rewrites the content of the document.  

	>>> db.update({"c":[0,1,2], "g": "The quick brown fox"}, id=1235)
	>>> db.all()
	{1: {'a':0}, 1235: {"c":[0,1,2], "g": "The quick brown fox"}}


All
---

.. code-block:: python

	piuma.All(
	    None
	) -> database: Dict

Returns the entire database.

	>>> db.all()
	{1: {'a':0}, 1235: {"c":[0,1,2], "g": "The quick brown fox"}}
