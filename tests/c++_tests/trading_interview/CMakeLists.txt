# Add the source files for the test executable
add_executable(test_arithmetic_mean
    test_arithmetic_mean.cpp
)

# Link the arithmetic_mean library to the test executable
target_link_libraries(test_arithmetic_mean arithmetic_mean)

# Include directories for the test executable
target_include_directories(test_arithmetic_mean PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../../../../src/c++_projects/trading_interview)