name = "houdini"

version = "20.5.654"

authors = [
    "SideFX"
]

description = \
    """
    Houdini is a 3D animation and visual effects (VFX) software renowned for its procedural workflow, which allows artists to create dynamic and complex simulations and effects in film, television, and games.
    """

tools = [
    "houdini",
    "hython"
]

requires = []

def commands():
    import platform

    if platform.system() == "Windows":
        env.PATH.append("C:\Program Files\Side Effects Software\Houdini 20.5.654")
    else:
        env.PATH.append("{root}/bin:{root}/python/bin")

        env.LD_LIBRARY_PATH.append("{root}/dsolib")

        env.HFS.set("{root}")
        env.HOUDINI_ROOT.set("{root}")

def post_commands():
    command("cd $HOUDINI_ROOT; source ./houdini_setup; cd -")

import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"