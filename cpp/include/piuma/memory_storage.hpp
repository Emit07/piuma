#pragma once
#include "storage.hpp"

namespace piuma {

class MemoryStorage : public Storage {
public:
    /**
     * A memory storage object for very fast reading and writing
     */
    MemoryStorage() : _memory(std::nullopt) {}

    std::optional<Database> read() override {
        return _memory;
    }

    void write(const Database& data) override {
        _memory = data;
    }

private:
    std::optional<Database> _memory;
};

} // namespace piuma
