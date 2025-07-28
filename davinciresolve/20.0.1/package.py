name = "davinciresolve"

version = "20.0.1"

installer = f"DaVinci_Resolve_{version}_Linux.zip"

tools = [
    "resolve"
]

build_command = f"""

if [ ! -f "{installer}" ]; then
    wget https://swr.cloud.blackmagicdesign.com/DaVinciResolve/v{version}/{installer}?verify=1753626023-q%2B%2BdcVxzJid2SJAbi96hglLD4F%2FmFmU%2FPFy2bR8BCR4%3D -O {installer}
fi

if [ -f "{installer}" ]; then
    unzip {installer} -n
    ./DaVinci_Resolve_{version}_Linux.run -i -y -n -C $REZ_BUILD_INSTALL_PATH
fi

"""

def commands():
    env.PATH.append("{root}/bin")
    env.DAVINCIRESOLVE_ROOT.set("{root}")

    alias("davinciresolve", "{root}/bin/resolve")

import platform

if platform.system() == "Windows":
    build_command = "{root}/build.bat"