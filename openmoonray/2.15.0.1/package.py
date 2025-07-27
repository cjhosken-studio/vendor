name = "openmoonray"

version = "2.15.0.1"

authors = [
    "Dreamworks Animation"
]

description = \
    """
    MoonRay is DreamWorks’ open-source, award-winning, state-of-the-art production MCRT renderer.
    """

tools = [

]

requires = [
    "studio_vfxplatform-2026",
    "openimageio-3",
    "openusd-25"
]

def commands():
    env.PATH.prepend("{root}/4.5/python/bin")
    env.PATH.prepend("{root}")

    if self.index == 0:
        env.PXR_PLUGINPATH_NAME.append("{root}/install/houdini/dso/usd_plugins")
    else:
        env.PXR_PLUGINPATH_NAME.append("{root}")
