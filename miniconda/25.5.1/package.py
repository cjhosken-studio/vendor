name = "miniconda"

version = "25.5.1"

authors = [
    "Anaconda"
]

description = \
    """
    Conda is a cross-platform, language-agnostic binary package manager.
    """

tools = [
    "conda"
]

def commands():
    import platform
    import pathlib

    if platform.system() == "Windows":
        miniconda_root = f"{pathlib.Path.home()}/miniconda3"

        env.PATH.prepend(f"{miniconda_root}/Scripts")

        if building:
            env.MINICONDA_ROOT.set(f"{miniconda_root}")
            env.MINICONDA_INCLUDE_DIR.set(f"{miniconda_root}/include")
            env.MINICONDA_LIBRARY_DIR.set(f"{miniconda_root}/Lib")
    
    else:
        env.PATH.prepend("{root}")
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

        if building:
            env.MINICONDA_ROOT.set("{root}")
            env.MINICONDA_INCLUDE_DIR.set("{root}/include")
            env.MINICONDA_LIBRARY_DIR.set("{root}/lib")

import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"