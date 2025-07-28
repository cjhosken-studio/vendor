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
    env.PATH.prepend("{root}")        
    env.VSCODE_ROOT.set("{root}")
    
    alias("vscode", "{root}/code")


import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"
else:
    build_command = "{root}/build.sh"