name = "houdini"

version = "20.5.654"

authors = [
    "SideFX"
]

description = \
    """
    Houdini is a 3D animation and visual effects (VFX) software renowned for its procedural workflow, which allows artists to create dynamic and complex simulations and effects in film, television, and games.
    """

tools = [
    "houdini",
    "hython"
]

requires = [
]

installer = "houdini-{version}-linux_x86_64_gcc11.2"

build_command=f"""

# Download installer if not present
if [ ! -f "{installer}.tar.gz" ]; then
    wget "https://example.com/stable/{installer}.tar.gz" -O "{installer}.tar.gz" || exit 1
fi
    
# Extract and install if download succeeded
if [ -f "{installer}.tar.gz" ]; then
    tar -xzf "{installer}.tar.gz" || exit 1
    "{installer}/houdini.install" --install-houdini \
        --install-sidefxlabs \
        --sidefxlabs-dir "$REZ_BUILD_INSTALL_PATH/SideFXLabs" \
        --no-root-check \
        "$REZ_BUILD_INSTALL_PATH" || exit 1
fi

# Create directory for splash images if it doesn't exist
mkdir -p "$REZ_BUILD_INSTALL_PATH/houdini/pic/"

rm -rf $REZ_BUILD_INSTALL_PATH/houdini/pic/*splash.pic*

# Convert and copy splash screens
for png in ../splash/*.png; do
    if [ -f "$png" ]; then
        BASE=$(basename "$png" .png)
        $REZ_BUILD_INSTALL_PATH/bin/iconvert "$png" "$REZ_BUILD_INSTALL_PATH/houdini/pic/$BASE.pic" || exit 1
    fi
done

# Copy all PNGs (including any not converted to .pic)
cp -r ../splash/* $REZ_BUILD_INSTALL_PATH/houdini/pic/
"""

def commands():
    env.PATH.append("{root}/bin:{root}/python/bin")

    env.LD_LIBRARY_PATH.append("{root}/dsolib")

    env.HFS.set("{root}")
    env.HOUDINI_ROOT.set("{root}")

def post_commands():
    command("cd $HOUDINI_ROOT; source ./houdini_setup; cd -")