cmake_minimum_required(VERSION 3.5)
project(PersonalProjects)

# Enabling compile_commands.json generation
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Enabling clang-tidy
set(CMAKE_CXX_CLANG_TIDY "clang-tidy;-checks=*")

# Specifying the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Adding subdirectories for different projects
add_subdirectory(src/c++_projects/trading_interview)
add_subdirectory(tests/c++_tests/trading_interview)