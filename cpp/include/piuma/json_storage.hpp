#pragma once
#include "storage.hpp"
#include <string>
#include <fstream>
#include <filesystem>

namespace piuma {

class JSONStorage : public Storage {
public:
    /**
     * If the database file does not exist it is created. A handle object is
     * created to talk to the database file
     *
     * @param path The path of the database file ie, "data/database.json".
     * @param makedirs Make directories leading to the database file if they do not exist.
     */
    JSONStorage(const std::string& path, bool makedirs = false);
    ~JSONStorage();

    std::optional<Database> read() override;
    void write(const Database& data) override;
    void close() override;

private:
    std::string _path;
    std::fstream _handle;
};

} // namespace piuma
