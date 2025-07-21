name = "openrv"

version = "3.0.0"

authors = [
    "Academy Software Foundation"
]

description = \
    """
    Open RV is an image and sequence viewer for VFX and animation artists. 
    Open RV is high-performant, hardware accelerated, and pipeline-friendly.
    """

variants = [
    ["vfxbase-2026", "qt-6.8", "openexr-3.3+"],
]

tools = [
    ""
]

requires = [
    "git",
]

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake")

    env.OpenRV_ROOT.set("{root}")