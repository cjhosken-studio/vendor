cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    openmoonray
    GIT_REPOSITORY https://github.com/dreamworksanimation/openmoonray.git
    GIT_TAG openmoonray-${VERSION}
    PREFIX openmoonray
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=ON
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] openmoonray-${VERSION} Install finished!\n\"
    )"
)