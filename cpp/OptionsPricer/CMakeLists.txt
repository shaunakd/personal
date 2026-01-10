cmake_minimum_required(VERSION 3.16)
project(OptionsPricer LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
option(BUILD_TESTS "Build OptionsPricer tests" OFF)

file(GLOB OPTIONSPRICER_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

# Exclude main.cpp from the library sources if present
list(FILTER OPTIONSPRICER_SOURCES EXCLUDE REGEX "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp$")

add_library(OptionsPricerLib ${OPTIONSPRICER_SOURCES})

target_include_directories(OptionsPricerLib
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

target_compile_options(OptionsPricerLib PRIVATE -Wall -Wextra -Wpedantic)

if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp)
  add_executable(pricer_main src/main.cpp)
  target_link_libraries(pricer_main PRIVATE OptionsPricerLib)
endif()

if(BUILD_TESTS)
  enable_testing()
  # tests go here
endif()

include(GNUInstallDirs)
install(TARGETS OptionsPricerLib RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR} LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR} ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR})
install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
