cmake_minimum_required(VERSION 3.10)
project(piuma CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find nlohmann/json (using the one we downloaded)
include_directories(include)

add_library(piuma_lib STATIC
    src/piuma.cpp 
    src/json_storage.cpp 
    src/cache.cpp
)
set_target_properties(piuma_lib PROPERTIES OUTPUT_NAME piuma)

# Tests
add_executable(test_piuma tests/test_piuma.cpp)
target_link_libraries(test_piuma piuma_lib)

add_executable(test_storage tests/test_storage.cpp)
target_link_libraries(test_storage piuma_lib)
