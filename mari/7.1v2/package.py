name = "mari"

version = "7.1v2"

authors = [
    "Foundry"
]

description = \
    """
    Mari is 3D painting without limits, combining the power and performance to handle even the most complex assets with artist-friendly 3D paint tools.
    """

tools = [
    "Mari7.1v2",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib:{root}/3rdParty/lib")

    alias("mari", "{root}/bin/Mari{version}")
    alias("mython", "{root}/3rdParty/python3.10")

import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"