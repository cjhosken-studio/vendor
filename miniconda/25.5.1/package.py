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

variants = [
    ["python-3.13"]
]

installer = f"Miniconda3-py313_{version}-1-Linux-x86_64.sh"

build_command = f"""
wget https://repo.anaconda.com/miniconda/{installer}
chmod +x ./{installer}
./{installer} -b -f -p $REZ_BUILD_INSTALL_PATH
"""

def commands():
    env.PATH.prepend("{root}")
    env.CMAKE_MODULE_PATH.append("{root}/cmake")

    env.miniconda_ROOT.set("{root}")
    env.miniconda_INCLUDE_DIR.set("{root}/include")
    env.miniconda_LIBRARY_DIR.set("{root}/lib")

