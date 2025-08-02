VERSION=$(basename "$(dirname "$0")")

INSTALLER="Mari$VERSION-linux-x86-release-64.run"

if [ ! -f $INSTALLER ]; then
    wget https://thefoundry.s3.amazonaws.com/products/mari/releases/{version}/{installer}
fi
if [ -f $INSTALLER ]; then
    chmod +x "./$INSTALLER"
    "./$INSTALLER" --prefix=$REZ_BUILD_INSTALL_PATH --accept-eula --exclude-subdir

    # Install the splash screen
    cp -r ../splash/* $REZ_BUILD_INSTALL_PATH/Media/Logos/
fi