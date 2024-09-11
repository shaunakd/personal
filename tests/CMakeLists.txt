cmake_minimum_required(VERSION 3.10)
project(TradingInterview)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 15)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the source files
set(SOURCES
    src/main.cpp
    src/arithmetic_mean.cpp
)

# Add the header files
set(HEADERS
    src/arithmetic_mean.h
)

# Create the executable
add_executable(TradingInterview ${SOURCES} ${HEADERS})

# Include the tests directory
add_subdirectory(tests)
