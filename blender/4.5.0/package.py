name = "blender"

version = "4.5.0"

authors = [
    "Blender Foundation"
]

description = \
    """
    Blender is a free and open-source 3D creation suite, used for a variety of tasks including modeling, animation, simulation, rendering, and video editing.
    """

tools = [
    "blender",
    "python",
    "python3",
    "python3.11"
]

requires = [
    "cmake-3.31.7+",
]

def commands():
    env.PATH.prepend("{root}/4.5/python/bin")
    env.PATH.prepend("{root}")

    alias("python", "{root}/4.5/python/bin/python3.11")
    alias("python3", "{root}/4.5/python/bin/python3.11")
    alias("bython", "{root}/4.5/python/bin/python3.11")