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

]

def commands():
    import platform
    env.PATH.prepend("{root}/4.5/python/bin")
    env.PATH.prepend("{root}")

    alias("blender", "{root}/blender --python-use-system-env --app-template blender")

    if platform.system() == "Windows":
        alias("python3", "{root}/4.5/python/bin/python")
    else:
        alias("python", "{root}/4.5/python/bin/python3.11")
        alias("python3", "{root}/4.5/python/bin/python3.11")

    if building:
        env.BLENDER_ROOT.set("{root}")
        
import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"