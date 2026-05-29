#include "piuma/json_storage.hpp"
#include <unistd.h>
#include <iostream>

namespace piuma {

JSONStorage::JSONStorage(const std::string& path, bool makedirs) : _path(path) {
    std::filesystem::path p(path);
    if (!std::filesystem::exists(p)) {
        if (makedirs && p.has_parent_path()) {
            std::filesystem::create_directories(p.parent_path());
        }
        // Create the file by opening it in append mode and closing it
        std::ofstream tmp(path, std::ios::app);
    }
    _handle.open(path, std::ios::in | std::ios::out);
}

JSONStorage::~JSONStorage() {
    close();
}

std::optional<Database> JSONStorage::read() {
    if (!_handle.is_open()) return std::nullopt;

    _handle.seekg(0, std::ios::end);
    auto size = _handle.tellg();

    if (size <= 0) {
        return std::nullopt;
    }

    _handle.seekg(0, std::ios::beg);
    _handle.clear(); // Clear any error flags like eof

    json j;
    try {
        _handle >> j;
    } catch (const std::exception& e) {
        return std::nullopt;
    }

    Database database;
    for (auto& [key, value] : j.items()) {
        try {
            database[std::stoi(key)] = value;
        } catch (...) {
            // Skip non-integer keys if any
        }
    }

    return database;
}

void JSONStorage::write(const Database& data) {
    if (!_handle.is_open()) return;

    _handle.seekg(0, std::ios::beg);
    _handle.clear();

    json j = json::object();
    for (auto const& [key, value] : data) {
        j[std::to_string(key)] = value;
    }

    std::string serialized = j.dump();
    _handle << serialized;
    _handle.flush();

    // Portably truncate is hard in std::fstream, use platform specific if available
    // On Linux we can use ftruncate
    int fd = -1;
#if defined(__linux__) || defined(__APPLE__)
    // This is a bit of a hack to get the file descriptor from fstream
    // but fstream doesn't provide it. We'll use the path instead.
    truncate(_path.c_str(), serialized.length());
#else
    // Fallback: close and reopen with trunc if not on Linux/Mac
    // For this translation, we'll assume POSIX for now as per session context.
#endif
}

void JSONStorage::close() {
    if (_handle.is_open()) {
        _handle.close();
    }
}

} // namespace piuma
