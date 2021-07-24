
import json
import os
import io
from typing import Dict


class Document(Dict):

	def __init__(self, value: Dict, id):
		self.id = id
		super().__init__(value)


class Piuma:

	def __init__(self, path: str):

		self._storage = FileStorage(path)
		self._next_id = None


	def insert(self, data: Dict, id: int=None) -> None:

		database = self._storage.read()

		if not id:
			id = self._get_next_id()

		database[id] = data

		self._storage.write(database)


	def all(self) -> Dict:
		return self._storage.read()


	def _get_next_id(self) -> int:

		if self._next_id is not None:
			self._next_id += 1

			return self._next_id

		database = self._storage.read()
		self._next_id = max(int(key) for key in database.keys())+1

		return self._next_id



class IOError(Exception):
	pass


class FileStorage:

	def __init__(self, path: str):
		
		self._handle = open(path, "r+")


	def read(self) -> Dict:
		"""
		Reads file and returns json data
		"""

		# Moves cursor to the start of the file
		self._handle.seek(0)

		# Returns loaded json content of file
		return json.load(self._handle)


	def write(self, data: Dict) -> None:
		"""
		Writes json data to the file
		"""

		# Moves cursor to the start of the file
		self._handle.seek(0)

		# Serializes the data to json
		serialized = json.dumps(data)

		# https://github.com/msiemens/tinydb/blob/master/tinydb/storages.py
		try:
			# Writes the serialized data to file
			self._handle.write(serialized)
		except io.UnsupportedOperation:
			raise IOError

		# Ensures file is written to and truncates the file if it is shortened
		self._handle.flush()
		os.fsync(self._handle.fileno())
		self._handle.truncate()


	def close(self) -> None:
		self._handle.close()
