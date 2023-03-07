cmake_minimum_required(VERSION 3.21)
project(SDAlab6)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(SDAlab6
        DO.cpp
        DO.h
        Iterator.cpp
        Iterator.h
        SDAlab6.cpp
        TestExtins.cpp
        TestExtins.h
        TestScurt.cpp
        TestScurt.h)
