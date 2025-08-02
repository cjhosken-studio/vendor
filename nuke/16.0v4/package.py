name = "nuke"

version = "16.0v4"
maj, mnr = version.split('.')[0:2]

authors = [
    "Foundry"
]

description = \
    """
    Nuke is a powerful, node-based compositing and visual effects software developed by Foundry. It's widely used in the film and television industry for creating high-quality visual effects, from blockbuster movies to episodic content.
    """

tools = [
    f"Nuke{maj}.0",
]

def commands():
    import platform
    maj, mnr = f"{version}".split('.')[0:2]


    if platform.system() == "Windows":
        nuke_root = f"C:/Program Files/Nuke{version}"
        env.PATH.prepend(nuke_root)
        alias("nuke", f"Nuke{maj}.0")
    else:
        env.PATH.prepend("{root}")
        env.LD_LIBRARY_PATH.append("{root}:{root}/lib")
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

        alias("nuke", f"{{root}}/Nuke{maj}.0")

import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"