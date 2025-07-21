name = "houdini"

version = "20.5.332"

authors = [
    "SideFX"
]

description = \
    """
    Houdini is a 3D animation and visual effects (VFX) software renowned for its procedural workflow, which allows artists to create dynamic and complex simulations and effects in film, television, and games.
    """

tools = [
    "houdini",
]

requires = [
]

build_command=""

def pre_commands():
    command(f"cd $HOME/software/sidefx/hfs{version}/ && source ./houdini_setup_bash && cd -")

def commands():

    env.PATH.prepend(f"$HOME/software/sidefx/hfs{version}/bin")
    env.PATH.prepend(f"$HOME/software/sidefx/hfs{version}/python/bin")

    env.LD_LIBRARY_PATH.append(f"$HOME/software/sidefx/hfs{version}/dsolib")

    env.HFS.set(f"$HOME/software/sidefx/hfs{version}")
    env.HOUDINI_ROOT.set(f"$HOME/software/sidefx/hfs{version}")