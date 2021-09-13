Usage
=====

Insert
------
	
.. code-block:: python

	<Piuma>.insert(
	    document: dict,
	    id: Optional[int]
	) -> id: int:

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

	<Piuma>.get(
	    id: int,
	) -> Optional[dict]

Returns a document by the id. The document id field only takes in integers.

	>>> db.get(id=1)
	{'a':0}


Remove
------

.. code-block:: python

	<Piuma>.remove(
	    id: int,
	) -> None:

Removes a document by the specified id. The document id field only takes in integers.

	>>> db.remove(id=1234)


Update
------

.. code-block:: python

	<Piuma>.update(
	    document: dict,
	    id: int 
	) -> None:

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

Other Usage
===========

Storages
--------

When creating the Piuma database object you can pass in a custom storage object. This storage object must have a read() and a write(data) method.

.. code-block:: python

	from piuma.storage import Storage

	class LoggingMemoryStorage(Storage):

	    def __init__(self):
	        self._memory = None

	    def read(self) -> Optional[Dict[int, Dict[Any, Any]]]:
	    	print("read")
	        return self._memory

	    def write(self, data: Dict[int, Dict[Any, Any]]) -> None:
	    	print("write")
	        self._memory = data

Once this custom memory is written you can pass in the class when creating the Piuma object. When passing through the custom storage object make sure to call it.

	>>> from piuma import Piuma
	>>> db = Piuma(storage=LoggingMemoryStorage())
	>>> db.insert({"a":0})
	read
	1
