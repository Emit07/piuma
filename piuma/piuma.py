
from typing import MutableMapping, Mapping, Dict, Callable, Optional, Any
from abc import ABC, abstractmethod


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
        Piuma `__init__` method, initializes the database by setting the
        storage object and the `_next_id`.

        Parameteres
        -----------
        storage: Storage, optional
            The storage object where the database is stored.
        """

        self._storage = storage
        self._next_id = int()

    def insert(self, value: Mapping, id: int = int()) -> int:
        """
        Inserts a new document into the database.

        Parameters
        ----------
        value: Mapping
            The value of the document that will be inserted. The value can take
            in any `Mapping` type, the simplest example is `dict`.
        id: int, optional
            The id of the document. This parameter is optional, if no id is
            passed in an id will be generated.

        Returns
        -------
        int
            returns the id of the inserted document
        """

        if not id:
            id = self._get_next_id()
        else:
            self._next_id = id

        def updater(database: MutableMapping[Any, Any]):
            """
            A common update method that specifies how to modify the database.
            Inserts a new document into the database.
            """

            if id not in database:
                database[id] = value
            else:
                raise KeyError("Document with the specified id already exists")

        self._update_database(updater)

        return id

    def get(self, id: int) -> Optional[Dict]:
        """
        Returns a document with a specified id.

        Parameters
        ----------
        id: int
            The id of the document that will be searched for

        Returns
        -------
        dict
            Returns the document that has specified id if it exists, if it does
            not exist then it returns none.
        """

        database = self._storage.read()

        if not database:
            database = {}

        return database[id] if id in database else None

    def remove(self, id: int) -> None:
        """
        Removes the document with the specified id

        Parameters
        ----------
        id: int
            The id of the document that will be searched for
        """

        def updater(database: MutableMapping[Any, Any]):
            """
            A common update method that specifies how to modify the database.
            Removes the document with the specified id
            """

            database.pop(id)

        self._update_database(updater)

    def update(self, value: Mapping, id: int) -> None:
        """
        Updates the document with the specified id

        Parameters
        ----------
        value: Mapping
            The value that will replace the previous value of the specified
            document. The value can take in any `Mapping` type, the simplest
            example is `dict`.
        id: int
            The id of the document that will be searched for
        """

        def updater(database: MutableMapping[Any, Any]):
            """
            A common update method that specifies how to modify the database.
            If the document with the specified id exists, update it.
            """

            if id in database:
                database[id] = value
            else:
                # TODO should this not return an error or `None`?
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
            self._next_id = max(key for key in database.keys()) + 1
        else:
            self._next_id = 1

        return self._next_id

    def _update_database(self, updater: Callable) -> None:
        """
        Run `updater` method to update the database and initialize it if it is
        not already

        Parameters
        ----------
        updater: Callable
            A method that specifies how to update the database
        """

        database = self._storage.read()

        # Initializes database if empty
        if not database:
            database = {}

        # Applies changes to the database
        updater(database)

        self._storage.write(database)
