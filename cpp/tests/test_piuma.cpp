#include <iostream>
#include <cassert>
#include "piuma/piuma.hpp"
#include "piuma/memory_storage.hpp"

using namespace piuma;

void test_insert() {
    Piuma db;
    int id1 = db.insert({{"a", 0}});
    int id2 = db.insert({{"b", "1"}});
    int id3 = db.insert({{"c", {0, 1, 2}}});

    assert(id1 == 1);
    assert(id2 == 2);
    assert(id3 == 3);

    auto all = db.all();
    assert(all.has_value());
    assert((*all)[1]["a"] == 0);
    assert((*all)[2]["b"] == "1");
    assert((*all)[3]["c"].is_array());
}

void test_insert_return_id() {
    Piuma db;
    assert(db.insert({{"a", 0}}) == 1);
    assert(db.insert({{"b", "1"}}, 123) == 123);
    assert(db.insert({{"c", {0, 1, 2}}}) == 124);
}

void test_get() {
    Piuma db;
    db.insert({{"a", 0}});
    db.insert({{"b", "1"}});

    auto val1 = db.get(1);
    assert(val1.has_value());
    assert((*val1)["a"] == 0);

    auto val2 = db.get(2);
    assert(val2.has_value());
    assert((*val2)["b"] == "1");

    auto val3 = db.get(3);
    assert(!val3.has_value());
}

void test_remove() {
    Piuma db;
    db.insert({{"a", 0}});
    db.remove(1);
    assert(!db.get(1).has_value());
}

void test_update() {
    Piuma db;
    db.insert({{"a", 0}});
    db.update({{"a", 1}, {"x", -1}}, 1);
    
    auto val = db.get(1);
    assert((*val)["a"] == 1);
    assert((*val)["x"] == -1);
}

int main() {
    test_insert();
    test_insert_return_id();
    test_get();
    test_remove();
    test_update();
    std::cout << "All Piuma tests passed!" << std::endl;
    return 0;
}
