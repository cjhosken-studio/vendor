cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set(CMAKE_TLS_VERIFY OFF)

if (HOUDINI_ROOT)
    message(STATUS "Building hdCycles for Houdini")
    ExternalProject_Add(
        Cycles
        URL https://projects.blender.org/blender/cycles/archive/v${VERSION}.tar.gz
        PREFIX cycles
        INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
        CMAKE_ARGS
            -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
            -DCMAKE_BUILD_TYPE=Release
            -DBUILD_SHARED_LIBS=ON
            -DHOUDINI_ROOT=${HOUDINI_ROOT}
            -DWITH_LEGACY_LIBRARIES=ON
            -DPYTHON_VERSION="3.13"
            -DPYTHON_LIBRARY=${Python_LIBRARY_DIR}
            -DPYTHON_INCLUDE_DIR=${Python_INCLUDE_DIR}
    )

else()
    message(STATUS "Building hdCycles for USD")
    ExternalProject_Add(
        Cycles
        URL https://projects.blender.org/blender/cycles/archive/v${VERSION}.tar.gz
        PREFIX cycles
        INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
        CMAKE_ARGS
            -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
            -DCMAKE_BUILD_TYPE=Release
            -DBUILD_SHARED_LIBS=ON
            -DPXR_ROOT=${USD_ROOT}
    )
endif()

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] Cycles-${VERSION} Install finished!\n\"
    )"
)