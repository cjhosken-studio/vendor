name = "davinciresolve"

version = "20.0.1"

tools = [
    "resolve"
]

def commands():
    env.PATH.append("{root}/bin")
    env.DAVINCIRESOLVE_ROOT.set("{root}")

    alias("davinciresolve", "{root}/bin/resolve")

import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"