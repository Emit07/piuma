#pragma once
#include "storage.hpp"
#include "memory_storage.hpp"
#include <memory>
#include <functional>
#include <optional>

namespace piuma {

class Piuma {
public:
    /**
     * Piuma constructor, initializes the database by setting the
     * storage object and the `_next_id`.
     *
     * @param storage The storage object where the database is stored.
     */
    Piuma(std::shared_ptr<Storage> storage = std::make_shared<MemoryStorage>());

    /**
     * Inserts a new document into the database.
     *
     * @param value The value of the document that will be inserted.
     * @param id The id of the document. Optional, if 0 an id will be generated.
     * @return returns the id of the inserted document
     */
    int insert(const json& value, int id = 0);

    /**
     * Returns a document with a specified id.
     *
     * @param id The id of the document that will be searched for
     * @return Returns the document if it exists, otherwise std::nullopt.
     */
    std::optional<json> get(int id);

    /**
     * Removes the document with the specified id
     *
     * @param id The id of the document to be removed
     */
    void remove(int id);

    /**
     * Updates the document with the specified id
     *
     * @param value The value that will replace the previous value.
     * @param id The id of the document that will be updated
     */
    void update(const json& value, int id);

    /**
     * Returns the entire database
     */
    std::optional<Database> all();

private:
    int _get_next_id();
    void _update_database(std::function<void(Database&)> updater);

    std::shared_ptr<Storage> _storage;
    int _next_id;
};

} // namespace piuma
