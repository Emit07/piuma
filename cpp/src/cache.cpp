#include "piuma/cache.hpp"

namespace piuma {

Cache::Cache(std::shared_ptr<Storage> storage, int max_modifications)
    : _storage(storage), _memory(std::nullopt), _max_modifications(max_modifications), _modifications(0) {}

Cache::~Cache() {
    close();
}

std::optional<Database> Cache::read() {
    return _memory;
}

void Cache::write(const Database& data) {
    _memory = data;
    _modifications++;

    if (_modifications > _max_modifications) {
        flush();
    }
}

void Cache::flush() {
    if (_memory.has_value()) {
        _storage->write(_memory.value());
    }
    _modifications = 0;
}

void Cache::close() {
    flush();
    _storage->close();
}

} // namespace piuma
