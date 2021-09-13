import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, Mapping, MutableMapping, Optional


class Storage(ABC):
    """
    An abstract class for all storages. This class ensures that any storage
    class has a read and a write method.
    """

    @abstractmethod
    def read(self) -> Optional[MutableMapping[Any, Any]]:
        """
        The read method should return the entire database, can optionally
        return None for initialization. If any data needs to be deserialized,
        it can be done here.
        """

        raise NotImplementedError("Not Overwritten")

    @abstractmethod
    def write(self, data: Mapping[Any, Any]) -> None:
        """
        The write method take in the entire database and write it. If any data
        needs to be serialized, it can be done here.
        """

        raise NotImplementedError("Not Overwritten")

    def close(self):
        """
        Optional Close mtheod to close any lingering handles
        """

        pass


class Cache:
    def __init__(self, storage: Storage, max_modifications: int = 500):
        """
        A Cache object that will act as a middleware by storing the data in
        memory and then writing to the storage object after a number of
        modifications.
        """

        self._storage = storage

        self._memory = None

        # Number of modifications before it writes to the storage
        self._max_modifications = max_modifications
        # Number of modifications
        self._modifications = 0

    def read(self):
        # Returns cached memory
        return self._memory

    def write(self, data):
        # Sets memory cache to data
        self._memory = data

        self._modifications += 1

        # If the modifications surpass the max modifications write to the file
        if self._modifications > self._max_modifications:
            self.flush()

    def flush(self):
        # Writes to file
        self._storage.write(self._memory)

        # Resets modifications
        self._modifications = 0

    def close(self):
        self.flush()

        self._storage.close()


class JSONStorage(Storage):
    def __init__(self, path: str, makedirs: bool = False):
        """
        If the database file does not exist it is created. A handle object is
        created to talk to the database file

        Parameters
        ----------
        path: str
            The path of the database file ie, "data/database.json".
        makedirs: bool
            Make directories leading to the database file if they do not exist.
        """

        if not os.path.exists(path):
            if makedirs:
                os.makedirs(os.path.dirname(path))

            with open(path, "a"):
                pass

        self._handle = open(path, mode="r+", encoding="utf-8")

    def read(self) -> Optional[MutableMapping[int, Dict[Any, Any]]]:
        # Gets the size so no error is returned if an empty file is read
        self._handle.seek(0, os.SEEK_END)
        size = self._handle.tell()

        if not size:
            return None

        else:
            # Moves cursor to the beginning reads and deserializes the raw file
            self._handle.seek(0)
            raw = json.load(self._handle)

            # Converts all the ids from `str` to int
            database = {int(id): document for id, document in raw.items()}

            return database

    def write(self, data: Mapping[int, Dict[Any, Any]]) -> None:

        if not data:
            data = {}

        # Move cursor to the beginning
        self._handle.seek(0)

        # Serialize the file
        serialized = json.dumps(data)

        self._handle.write(serialized)

        # Makes sure the file is written to
        self._handle.flush()
        os.fsync(self._handle.fileno())

        # If the file has gotten shorter it removes any extra pieces
        self._handle.truncate()

    def close(self):
        self._handle.close()
