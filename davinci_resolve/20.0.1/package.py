name = "davinci_resolve"

version = "20.0.1"

description = \
    """

    """

tools = [
    "resolve",
    "davinci_resolve"
]

def commands():
    import platform

    if platform.system() == "Windows":
        resolve_root = "C:/Program Files/Blackmagic Design/DaVinci Resolve"
        env.PATH.append(f"{resolve_root}")
        env.DAVINCI_RESOLVE_ROOT.set(f"{resolve_root}")
        alias("davinci_resolve", f"Resolve.exe")
        alias("resolve", f"Resolve.exe")
    
    else:
        env.PATH.append("{root}/bin")
        env.DAVINCI_RESOLVE_ROOT.set("{root}")
        alias("davinci_resolve", "{root}/bin/resolve")

import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"