name = "mari"

version = "7.1"

authors = [
    "SideFX"
]

description = \
    """
    Mari is 3D painting without limits, combining the power and performance to handle even the most complex assets with artist-friendly 3D paint tools.
    """

tools = [
    "Mari7.1v2",
]

requires = [
]

build_command=""

def commands():
    minor_version = "v2"

    env.PATH.prepend(f"$HOME/software/foundry/Mari{version}{minor_version}/bin")
    env.LD_LIBRARY_PATH.append(f"$HOME/software/foundry/Mari{version}{minor_version}/lib:$HOME/software/foundry/Mari{version}{minor_version}/3rdParty/lib")


    alias("mari", f"$HOME/software/foundry/Mari{version}{minor_version}/mari")
    alias("mython", f"$HOME/software/foundry/Mari{version}{minor_version}/3rdParty/python3.10")