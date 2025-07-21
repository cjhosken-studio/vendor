cmake_minimum_required(VERSION 3.31.7)

include(RezBuild)
include(ExternalProject)

get_filename_component(VERSION ${CMAKE_CURRENT_SOURCE_DIR} NAME)

# Extract major.minor version (e.g., "3.6" from "3.6.5")
string(REGEX REPLACE "^([0-9]+\\.[0-9]+).*" "\\1" VERSION_MAJOR_MINOR ${VERSION})

ExternalProject_Add(
    blender
    URL https://download.blender.org/release/Blender${VERSION_MAJOR_MINOR}/blender-${VERSION}-linux-x64.tar.xz
    PREFIX blender
    INSTALL_DIR $ENV{REZ_BUILD_INSTALL_PATH}
    CONFIGURE_COMMAND ""  # No configuration needed for pre-built binary
    BUILD_COMMAND ""      # No build needed for pre-built binary
    BUILD_IN_SOURCE 0
    INSTALL_COMMAND 
        COMMAND ${CMAKE_COMMAND} -E make_directory <INSTALL_DIR>
        COMMAND ${CMAKE_COMMAND} -E tar xf <DOWNLOAD_DIR>/blender-${VERSION}-linux-x64.tar.xz
        COMMAND ${CMAKE_COMMAND} -E copy_directory <SOURCE_DIR> <INSTALL_DIR>
)

install(
    CODE
    "execute_process(
        COMMAND echo \"\n[REZ] blender-${REZ_BUILD_PROJECT_VERSION} Install finished!\n\"
    )"
)