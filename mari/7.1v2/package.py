name = "mari"

version = "7.1v2"

authors = [
    "Foundry"
]

description = \
    """
    Mari is 3D painting without limits, combining the power and performance to handle even the most complex assets with artist-friendly 3D paint tools.
    """

tools = [
    "Mari7.1v2",
]

requires = [
]

installer=f"Mari{version}-linux-x86-release-64.run"

build_command=f"""
if [ ! -f "{installer}" ]; then
    wget https://thefoundry.s3.amazonaws.com/products/mari/releases/{version}/{installer}
fi
if [ -f "{installer}" ]; then
    chmod +x ./{installer}
    ./{installer} --prefix=$REZ_BUILD_INSTALL_PATH --accept-eula --exclude-subdir

    # Install the splash screen
    cp -r ../splash/* $REZ_BUILD_INSTALL_PATH/Media/Logos/
fi
"""

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib:{root}/3rdParty/lib")

    alias("mari", "{root}/bin/Mari{version}")
    alias("mython", "{root}/3rdParty/python3.10")