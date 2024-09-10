# Add the source files for the arithmetic mean project
add_library(arithmetic_mean
    arithmetic_mean.cpp
)

# Include directories for the arithmetic mean project
target_include_directories(arithmetic_mean PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})