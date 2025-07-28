name = "nuke"

version = "16.0v4"

authors = [
    "Foundry"
]

description = \
    """
    Nuke is a powerful, node-based compositing and visual effects software developed by Foundry. It's widely used in the film and television industry for creating high-quality visual effects, from blockbuster movies to episodic content.
    """

tools = [
    "Nuke16.0",
]

def commands():
    env.PATH.prepend("{root}")
    env.LD_LIBRARY_PATH.append("{root}:{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    alias("nuke", "{root}/Nuke16.0")
    alias("nython", "{root}/python3")

import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"