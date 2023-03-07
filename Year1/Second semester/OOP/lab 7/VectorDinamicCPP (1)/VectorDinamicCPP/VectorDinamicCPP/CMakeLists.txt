cmake_minimum_required(VERSION 3.16)
project(VectorDinamicCPP)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(VectorDinamicCPP
        main.cpp
        Pet.cpp
        Pet.h
        VectDinNewDelete.cpp
        VectDinNewDelete.h
        VectDinSmartPointer.cpp
        VectDinSmartPointer.h
        VectorDinamicTemplate.h VectorDinamicIlinca.h)
