name = "davinciresolve"

version = "20.0.1"

description = \
    """

    """

tools = [
    "resolve",
    "davinciresolve"
]

def commands():
    import platform

    if platform.system() == "Windows":
        resolve_root = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve"
        env.PATH.append(f"{resolve_root}")
        env.DAVINCIRESOLVE_ROOT.set(f"{resolve_root}")
        alias("davinciresolve", f"Resolve.exe")
        alias("resolve", f"Resolve.exe")
    
    else:
        env.PATH.append("{root}/bin")
        env.DAVINCIRESOLVE_ROOT.set("{root}")
        alias("davinciresolve", "{root}/bin/resolve")

import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"