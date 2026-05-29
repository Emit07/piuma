#include "piuma/piuma.hpp"
#include <stdexcept>
#include <algorithm>

namespace piuma {

Piuma::Piuma(std::shared_ptr<Storage> storage) : _storage(storage), _next_id(0) {}

int Piuma::insert(const json& value, int id) {
    if (id == 0) {
        id = _get_next_id();
    } else {
        _next_id = id;
    }

    auto updater = [id, value](Database& database) {
        if (database.find(id) == database.end()) {
            database[id] = value;
        } else {
            throw std::runtime_error("Document with the specified id already exists");
        }
    };

    _update_database(updater);
    return id;
}

std::optional<json> Piuma::get(int id) {
    auto database = _storage->read();
    if (!database) return std::nullopt;

    if (database->find(id) != database->end()) {
        return database->at(id);
    }
    return std::nullopt;
}

void Piuma::remove(int id) {
    auto updater = [id](Database& database) {
        database.erase(id);
    };
    _update_database(updater);
}

void Piuma::update(const json& value, int id) {
    auto updater = [id, value](Database& database) {
        if (database.find(id) != database.end()) {
            database[id] = value;
        } else {
            throw std::out_of_range("Id not found: " + std::to_string(id));
        }
    };
    _update_database(updater);
}

std::optional<Database> Piuma::all() {
    return _storage->read();
}

int Piuma::_get_next_id() {
    if (_next_id != 0) {
        _next_id++;
        return _next_id;
    }

    auto database = _storage->read();
    if (database && !database->empty()) {
        int max_id = 0;
        for (auto const& [key, _] : *database) {
            if (key > max_id) max_id = key;
        }
        _next_id = max_id + 1;
    } else {
        _next_id = 1;
    }
    return _next_id;
}

void Piuma::_update_database(std::function<void(Database&)> updater) {
    auto database_opt = _storage->read();
    Database database;
    if (database_opt) {
        database = *database_opt;
    }

    updater(database);
    _storage->write(database);
}

} // namespace piuma
