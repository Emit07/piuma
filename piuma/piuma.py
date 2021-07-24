
import json
import os
import io
from typing import Dict


class Piuma:

	def __init__(self, path: str):

		self._storage = FileStorage(path)


	def all(self) -> Dict:
		return self._storage.read()


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
		# self._handle.seek(0)

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
