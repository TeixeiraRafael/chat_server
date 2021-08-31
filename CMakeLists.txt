cmake_minimum_required(VERSION 3.10)

project(chat_server VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

file(
    GLOB
    SOURCES
    "src/main.cpp"
)

file(
    GLOB
    HEADERS
    "include/definitions.h"
)
    

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE include)
target_link_libraries(${PROJECT_NAME} pthread)