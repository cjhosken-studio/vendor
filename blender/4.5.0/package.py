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

build_command = f"""
wget https://download.blender.org/release/Blender4.5/blender-{version}-linux-x64.tar.xz
tar -xf blender-{version}-linux-x64.tar.xz -C "$REZ_BUILD_INSTALL_PATH" --strip-components=1
"""

def commands():
    env.PATH.prepend("{root}/4.5/python/bin")
    env.PATH.prepend("{root}")

    alias("python", "{root}/4.5/python/bin/python3.11")
    alias("python3", "{root}/4.5/python/bin/python3.11")
    alias("bython", "{root}/4.5/python/bin/python3.11")