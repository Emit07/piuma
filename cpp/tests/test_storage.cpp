#include <iostream>
#include <cassert>
#include <filesystem>
#include "piuma/json_storage.hpp"
#include "piuma/piuma.hpp"

using namespace piuma;

void test_json_storage() {
    const std::string filename = "test_db.json";
    if (std::filesystem::exists(filename)) {
        std::filesystem::remove(filename);
    }

    {
        JSONStorage storage(filename);
        Piuma db(std::make_shared<JSONStorage>(filename));
        db.insert({{"a", 1}});
        db.insert({{"b", 2}});
    } // Close and flush

    {
        Piuma db(std::make_shared<JSONStorage>(filename));
        auto all = db.all();
        assert(all.has_value());
        assert((*all).size() == 2);
        assert((*all)[1]["a"] == 1);
        assert((*all)[2]["b"] == 2);
    }

    std::filesystem::remove(filename);
}

int main() {
    test_json_storage();
    std::cout << "All Storage tests passed!" << std::endl;
    return 0;
}
