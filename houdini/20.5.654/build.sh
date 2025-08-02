VERSION=$(basename "$(dirname "$0")")

GCC_VERSION=11.2

INSTALLER="houdini-$VERSION-linux_x86_64_gcc$GCC_VERSION"

# Download installer if not present
if [ ! -f "$INSTALLER.tar.gz" ]; then
    wget "https://example.com/stable/$INSTALLER.tar.gz" -O "$INSTALLER.tar.gz" || exit 1
fi
    
# Extract and install if download succeeded
if [ -f "$INSTALLER.tar.gz" ]; then
    tar -xzf "$INSTALLER.tar.gz" || exit 1
    "$INSTALLER/houdini.install" --install-houdini \
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