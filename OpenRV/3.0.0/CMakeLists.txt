cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

ExternalProject_Add(
    OpenRV
    GIT_REPOSITORY https://github.com/AcademySoftwareFoundation/OpenRV.git
    GIT_TAG feature/qt6 #v{VERSION} OpenRV v3.0.0 hasnt officially been released yet
    GIT_SUBMODULES_RECURSE ON  # This enables recursive submodule cloning
    GIT_SHALLOW OFF
    PREFIX openrv
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_CXX_STANDARD=17
        -DBUILD_SHARED_LIBS=ON

        -DRV_DEPS_QT6_LOCATION=${Qt_ROOT}
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] OpenRV-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)