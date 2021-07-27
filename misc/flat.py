from typing import Dict, Callable
class Document(Dict):
	pass
class Piuma:
	def __init__(self, path: str=""):
		self._storage = MemoryStorage()
		self._next_id = None
	def insert(self, data: Dict, id: int=None) -> int:
		if not id:
			id = self._get_next_id()
		else:
			self._next_id = id
		def updater(database: Dict):
			database[id] = Document(data)
		self._update_database(updater)
		return id
	def get(self, id: int) -> Dict:
		return self._storage.read()[id]
	def remove(self, id: int) -> None:
		def updater(database: Dict):
			database.pop(id)
		self._update_database(updater)
	def update(self, data: Dict, id: int) -> None:
		def updater(database: Dict):
			if id in database:
				database[id] = Document(data)
			else:
				raise KeyError(id)
		self._update_database(updater)
	def all(self) -> Dict:
		return self._storage.read()
	def _get_next_id(self) -> int:
		if self._next_id is not None:
			self._next_id += 1
			return self._next_id
		database = self._storage.read()
		if not database:
			self._next_id = 1
		else:
			self._next_id = max(int(key) for key in database.keys())+1
		return self._next_id
	def _update_database(self, updater: Callable) -> None:
		database = self._storage.read()
		if not database:
			databse = {}
		updater(database)
		self._storage.write(database)
class MemoryStorage:
	def __init__(self):
		self._memory = None
	def read(self) -> Dict:
		return self._memory
	def write(self, data: Dict) -> None:
		self._memory = data