VERSION=$(basename "$(dirname "$0")")

INSTALLER="Nuke$VERSION-linux-x86_64.tgz"

if [ ! -f "$INSTALLER" ]; then
    wget https://thefoundry.s3.amazonaws.com/products/nuke/releases/$VERSION/$INSTALLER
fi

if [ -f "$INSTALLER" ]; then
    tar -xzf $INSTALLER
    "./Nuke$VERSION-linux-x86_64.run" --prefix=$REZ_BUILD_INSTALL_PATH --accept-foundry-eula --exclude-subdir

    # Install the splash screen
    cp -r ../splash/* $REZ_BUILD_INSTALL_PATH/Resources/SplashScreens/
fi