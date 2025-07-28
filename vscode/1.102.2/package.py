name = "vscode"

version = "1.102.2"

description = \
    """
    Visual Studio Code, commonly referred to as VS Code, is an integrated development environment developed by Microsoft for Windows, Linux, macOS and web browsers.
    """

authors = [
    "Microsoft"
]

build_command = f"""
wget https://update.code.visualstudio.com/{version}/linux-x64/stable -O vscode.tgz

if [ -f vscode.tgz ]; then
    tar -xzf vscode.tgz -C $REZ_BUILD_INSTALL_PATH --strip-components=1
fi
"""

def commands():
    env.PATH.prepend("{root}")        
    env.VSCODE_ROOT.set("{root}")
    
    alias("vscode", "{root}/code")


import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"