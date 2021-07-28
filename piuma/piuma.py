
from typing import Dict, Callable


class Document(Dict):
	"""
	Boiler-plate for all documents or "entries" in the database
	You can add attributes and functions if you want a more developed document
	"""
	pass


class Piuma:

	def __init__(self, path: str=""):
		"""
		Main Class of Piuma

		This class creates the storage object and does the formatting and
		parsing of the data stored in the storage object. This main class does
		not include a query. 
		"""
		
		# Storage object can be swapped with an object that writes to a json file
		self._storage = MemoryStorage()
		self._next_id = None


	def insert(self, data: Dict, id: int=None) -> int:
		"""
		Inserts a new document into the database

		<data>: the data that the document will hold
		<id>: the id of the document(optional)
		"""

		# If the id is not specified then generate an id
		if not id:
			id = self._get_next_id()
		else:
			self._next_id = id

		def updater(database: Dict):
			"""
			Specifies how to modify the database

			Adds the document with the key of <id> 

			TODO this could cause conflict if the specified id already exists
			"""

			database[id] = Document(data)

		self._update_database(updater)

		return id


	def get(self, id: int) -> Dict:
		"""
		Returns Document by id

		TODO make better??
		"""

		return self._storage.read()[id]


	def remove(self, id: int) -> None:
		"""
		Removes the document with the specified id

		<id>: the id of the document
		"""

		def updater(database: Dict):
			# Removes document with existing id

			database.pop(id)

		self._update_database(updater)


	def update(self, data: Dict, id: int) -> None:
		"""
		Updates the document with the specified id

		<data>: the new data of the document that will be updated
		<id>: the id of the document that needs to be updated
		"""

		def updater(database: Dict):
			# if the document is valid then update it
			if id in database:
				database[id] = Document(data)
			else:
				raise KeyError(id)

		self._update_database(updater)


	def all(self) -> Dict:
		return self._storage.read()


	def _get_next_id(self) -> int:
		"""
		Returns the next available id in the database 

		TODO a lot of this function seems inefficient, try to slim down
		"""

		# If _next_id is already initialized then add one and return
		if self._next_id is not None:
			self._next_id += 1

			return self._next_id

		database = self._storage.read()

		# if the database is empty then _next_id is 1
		if not database:
			self._next_id = 1
		else:
			# if the database is not empty the _next_id is 1 more than the
			# biggest id 
			self._next_id = max(int(key) for key in database.keys())+1

		return self._next_id


	def _update_database(self, updater: Callable) -> None:
		"""
		A tinydb (https://github.com/msiemens/tinydb) style update class to
		update the database and initialize it if it is not already

		<updater>: a function that specifies how to update the database
		"""

		database = self._storage.read()

		# Initializes the database if it is empty
		if not database:
			database = {}

		# Applies changes to the database
		updater(database)

		self._storage.write(database)


class MemoryStorage:

	def __init__(self):
		"""
		A memory storage object for very fast reading and writing
		"""
		self._memory = None


	def read(self) -> Dict:
		return self._memory


	def write(self, data: Dict) -> None:
		self._memory = data
