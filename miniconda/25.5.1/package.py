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

    if platform.system() == "Windows":
        env.PATH.prepend("{root}/Scripts")

        env.miniconda_ROOT.set("{root}")
        env.miniconda_INCLUDE_DIR.set("{root}/include")
        env.miniconda_LIBRARY_DIR.set("{root}/Lib")
    
    else:
        env.PATH.prepend("{root}")
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

        env.miniconda_ROOT.set("{root}")
        env.miniconda_INCLUDE_DIR.set("{root}/include")
        env.miniconda_LIBRARY_DIR.set("{root}/lib")

import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"