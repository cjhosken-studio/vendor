name = "vscode"

version = "1.102.2"

description = \
    """
    Visual Studio Code, commonly referred to as VS Code, is an integrated development environment developed by Microsoft for Windows, Linux, macOS and web browsers.
    """

authors = [
    "Microsoft"
]

def commands():
    import platform
    import pathlib
    
    if platform.system() == "Windows":
        code_root = f"{pathlib.Path.home()}/AppData/Local/Programs/Microsoft VS Code"
        env.PATH.prepend(f"{code_root}")
        env.VSCODE_ROOT.set(f"{code_root}")
        alias("vscode", "Code.exe")
    else:
        env.PATH.prepend("{root}")        
        env.VSCODE_ROOT.set("{root}")
        
        alias("vscode", "{root}/code")


import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"