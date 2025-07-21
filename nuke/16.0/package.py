name = "nuke"

version = "16.0"

authors = [
    "SideFX"
]

description = \
    """
    Nuke is a powerful, node-based compositing and visual effects software developed by Foundry. It's widely used in the film and television industry for creating high-quality visual effects, from blockbuster movies to episodic content.
    """

tools = [
    "Nuke16.0",
]

requires = [
]

build_command=""

def commands():
    minor_version = "v4"
    env.PATH.prepend(f"$HOME/software/foundry/Nuke{version}{minor_version}")
    env.LD_LIBRARY_PATH.append(f"$HOME/software/foundry/Nuke{version}{minor_version}")


    alias("nuke", f"$HOME/software/foundry/Nuke{version}{minor_version}/Nuke{version}")
    alias("nython", f"$HOME/software/foundry/Nuke{version}{minor_version}/python3")