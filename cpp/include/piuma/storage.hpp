#pragma once
#include <optional>
#include <map>
#include <nlohmann/json.hpp>

namespace piuma {

using json = nlohmann::json;
using Database = std::map<int, json>;

class Storage {
public:
    virtual ~Storage() = default;

    /**
     * The read method should return the entire database, can optionally
     * return std::nullopt for initialization.
     */
    virtual std::optional<Database> read() = 0;

    /**
     * The write method take in the entire database and write it.
     */
    virtual void write(const Database& data) = 0;

    /**
     * Optional Close method to close any lingering handles
     */
    virtual void close() {}
};

} // namespace piuma
