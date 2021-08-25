
from typing import MutableMapping, Mapping, Dict, Callable, Optional, Any
from abc import ABC, abstractmethod


class Storage(ABC):
    """
    A Base class for all storages
    """

    @abstractmethod
    def read(self) -> Optional[MutableMapping[Any, Any]]:
        """
        The read method should return the entire database, can optionally
        return None for initialization
        """

        raise NotImplementedError("Not Overwritten")

    @abstractmethod
    def write(self, data: Mapping[Any, Any]) -> None:
        """
        The write method take in the entire database and write it.
        """
        raise NotImplementedError("Not Overwritten")


class MemoryStorage(Storage):

    def __init__(self):
        """
        A memory storage object for very fast reading and writing
        """
        self._memory = None

    def read(self) -> Optional[MutableMapping[Any, Any]]:
        return self._memory

    def write(self, data: Mapping[Any, Any]) -> None:
        self._memory = data


class Piuma:

    def __init__(self, storage: Storage = MemoryStorage()):
        """
        Main Class of Piuma

        This class creates the storage object and does the formatting and
        parsing of the data stored in the storage object.
        """

        self._storage = storage
        self._next_id = int()

    def insert(self, data: Mapping, id: int = int()) -> int:
        """
        Inserts a new document into the database

        <data>: the data that the document will hold
        <id>: the id of the document (optional)
        """

        if not id:
            id = self._get_next_id()
        else:
            self._next_id = id

        def updater(database: MutableMapping[Any, Any]):
            """
            Specifies how to modify the database

            Adds the document with the key of <id>

            TODO this could cause conflict if the specified id already exists
            """

            if id in database:
                raise KeyError("Document with the specified id already exists")

            else:
                database[id] = data

        self._update_database(updater)

        return id

    def get(self, id: int) -> Dict:
        """
        Returns Document by id

        <id>: the id of the document
        """

        database = self._storage.read()

        if not database:
            database = {}

        return database[id] if id in database else None

    def remove(self, id: int) -> None:
        """
        Removes the document with the specified id

        <id>: the id of the document
        """

        def updater(database: MutableMapping[Any, Any]):
            # Removes document with given id

            database.pop(id)

        self._update_database(updater)

    def update(self, data: Mapping, id: int) -> None:
        """
        Updates the document with the specified id

        <data>: the new data of the document that will be updated
        <id>: the id of the document that needs to be updated
        """

        def updater(database: MutableMapping[Any, Any]):
            # if the document is valid then update it
            if id in database:
                database[id] = data
            else:
                # TODO should this not return an error?
                raise KeyError(id)

        self._update_database(updater)

    def all(self) -> Optional[MutableMapping[Any, Any]]:
        return self._storage.read()

    def _get_next_id(self) -> int:
        """
        Returns the next available id in the database
        """

        if self._next_id is not None:
            self._next_id += 1

            return self._next_id

        database = self._storage.read()

        # if the database is empty then _next_id is 1
        if database:
            # the _next_id is 1 more than the biggest id
            self._next_id = max(key for key in database.keys())+1
        else:
            self._next_id = 1

        return self._next_id

    def _update_database(self, updater: Callable) -> None:
        """
        A tinydb (https://github.com/msiemens/tinydb) style update class to
        update the database and initialize it if it is not already

        <updater>: a function that specifies how to update the database
        """

        database = self._storage.read()

        # Initializes database if empty
        if not database:
            database = {}

        # Applies changes to the database
        updater(database)

        self._storage.write(database)
