name = "cycles"

version = "4.4.0"

authors = [
    "Blender Foundation"
]

description = \
    """
    Cycles is a path tracing renderer focused on interactivity and ease of use, while supporting many production features.
    """

tools = [

]

variants = [
    ["houdini-20.5"]
]

requires = [
    "python-3.13",
    "cmake-3.31.7+"
]

def commands():
    env.PATH.prepend("{root}/4.5/python/bin")
    env.PATH.prepend("{root}")

    if self.index == 0:
        env.PXR_PLUGINPATH_NAME.append("{root}/install/houdini/dso/usd_plugins")
    else:
        env.PXR_PLUGINPATH_NAME.append("{root}")
