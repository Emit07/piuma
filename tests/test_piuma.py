import unittest

from piuma import Piuma
from piuma.piuma import MemoryStorage
from typing import Dict


class Test_Piuma(unittest.TestCase):

    def setUp(self):
        self.db = Piuma()

    def test_storage(self):

        self.assertEqual(self.db._storage.__class__, MemoryStorage)

    def test_insert(self):

        self.db._storage.write(None)
        self._next_id = None

        self.db.insert({"a": 0})
        self.db.insert({"b": "1"})
        self.db.insert({"c": [0, 1, 2]})

        self.assertEqual({"a": 0}, self.db.all()[1])
        self.assertEqual({"b": "1"}, self.db.all()[2])
        self.assertEqual({"c": [0, 1, 2]}, self.db.all()[3])

    def test_insert_return_id(self):

        self.db._storage.write(None)
        self._next_id = None

        self.assertEqual(self.db.insert({"a": 0}), 1)
        self.assertEqual(self.db.insert({"b": "1"}, id=123), 123)
        self.assertEqual(self.db.insert({"c": [0, 1, 2]}), 124)

    def test_all(self):

        self.db._storage.write(None)
        self._next_id = None

        self.db.insert({"a": 0})

        self.assertEqual({1: {"a": 0}}, self.db.all())

        self.db.insert({"b": 1})

        self.assertEqual({1: {"a": 0}, 2: {"b": 1}}, self.db.all())

    def test_get(self):

        self.db._storage.write(None)
        self._next_id = None

        self.db.insert({"a": 0})
        self.db.insert({"b": "1"})
        self.db.insert({"c": [0, 1, 2]})

        self.assertEqual(self.db.get(id=1), {"a": 0})
        self.assertEqual(self.db.get(id=2), {"b": "1"})
        self.assertEqual(self.db.get(id=3), {"c": [0, 1, 2]})

    def test_remove(self):

        self.db._storage.write(None)
        self._next_id = None

        self.db.insert({"a": 0})
        self.db.insert({"b": "1"})
        self.db.insert({"c": [0, 1, 2]})

        self.assertEqual({"a": 0}, self.db.all()[1])
        self.assertEqual({"b": "1"}, self.db.all()[2])
        self.assertEqual({"c": [0, 1, 2]}, self.db.all()[3])

        self.db.remove(id=1)
        self.db.remove(id=2)
        self.db.remove(id=3)

        self.assertEqual(1 in self.db.all(), False)
        self.assertEqual(2 in self.db.all(), False)
        self.assertEqual(3 in self.db.all(), False)

    def test_update(self):

        self.db._storage.write(None)
        self._next_id = None

        self.db.insert({"a": 0})
        self.db.insert({"b": "1", "n": 2})
        self.db.insert({"c": [0, 1, 2]})

        self.assertEqual({"a": 0}, self.db.all()[1])
        self.assertEqual({"b": "1", "n": 2}, self.db.all()[2])
        self.assertEqual({"c": [0, 1, 2]}, self.db.all()[3])

        self.db.update({"a": 1, "x": -1}, id=1)
        self.db.update({"b": 1}, id=2)
        self.db.update({"c": [0, 1, 2, 3]}, id=3)

        self.assertEqual({"a": 1, "x": -1}, self.db.all()[1])
        self.assertEqual({"b": 1}, self.db.all()[2])
        self.assertEqual({"c": [0, 1, 2, 3]}, self.db.all()[3])

    def test_get_next_id(self):

        self.db._storage.write(None)
        self._next_id = None

        self.assertEqual(self.db._get_next_id(), 1)
        self.assertEqual(self.db._get_next_id(), 2)

        self.db._next_id = 123

        self.assertEqual(self.db._get_next_id(), 124)
        self.assertEqual(self.db._get_next_id(), 125)

        self.db.insert({})

        self.assertEqual(self.db._next_id, 126)

    def test_update_database(self):

        # TODO write more tests for update

        self.db._storage.write(None)
        self._next_id = None

        id = 1

        def update(database: Dict):

            database[id] = {"a": 0}

        self.db._update_database(update)

        self.assertEqual(self.db.all(), {1: {"a": 0}})


class Test_MemoryStorage(unittest.TestCase):

    def setUp(self):

        self._storage = MemoryStorage()

    def test_write(self):

        self.assertEqual(self._storage._memory, None)

        self._storage.write({})
        self.assertEqual(self._storage._memory, {})

        self._storage.write({"a": 0})
        self.assertEqual(self._storage._memory, {"a": 0})

    def test_read(self):

        self.assertEqual(self._storage.read(), self._storage._memory)
