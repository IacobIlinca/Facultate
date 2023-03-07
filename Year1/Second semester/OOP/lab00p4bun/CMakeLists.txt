cmake_minimum_required(VERSION 3.16)
project(lab00p4bun C)

set(CMAKE_C_STANDARD 11)

include_directories(lab00p4bun)

add_executable(lab00p4bun
        lab00p4bun/element.c
        lab00p4bun/element.h
        lab00p4bun/lista.c
        lab00p4bun/lista.h
        lab00p4bun/main.c
        lab00p4bun/service.c
        lab00p4bun/service.h
        lab00p4bun/teste.c
        lab00p4bun/teste.h repo.c repo.h)
