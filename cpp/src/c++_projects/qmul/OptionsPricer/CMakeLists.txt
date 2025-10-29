cmake_minimum_required(VERSION 3.16)
project(OptionsPricer LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(OptionsPricerLib
    src/OptionsPricer.cpp
)

target_include_directories(OptionsPricerLib
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_executable(options_pricer apps/pricer_main.cpp)
target_link_libraries(options_pricer PRIVATE OptionsPricerLib)

install(TARGETS OptionsPricerLib options_pricer
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
