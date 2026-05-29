#pragma once
#include "storage.hpp"
#include <memory>

namespace piuma {

class Cache : public Storage {
public:
    /**
     * A Cache object that will act as a middleware by storing the data in
     * memory and then writing to the storage object after a number of
     * modifications.
     */
    Cache(std::shared_ptr<Storage> storage, int max_modifications = 500);
    ~Cache();

    std::optional<Database> read() override;
    void write(const Database& data) override;
    void flush();
    void close() override;

private:
    std::shared_ptr<Storage> _storage;
    std::optional<Database> _memory;
    int _max_modifications;
    int _modifications;
};

} // namespace piuma
