VERSION=$(basename "$(dirname "$0")")

if [ ! -f "resolve-$VERSION.zip" ]; then
    wget https://swr.cloud.blackmagicdesign.com/DaVinciResolve/v$VERSION/DaVinci_Resolve_$VERSION_Linux.zip?verify=1753626023-q%2B%2BdcVxzJid2SJAbi96hglLD4F%2FmFmU%2FPFy2bR8BCR4%3D -O resolve-$VERSION.zip
fi

if [ -f "resolve-$VERSION.zip" ]; then
    unzip resolve-$VERSION.zip -n
    "./DaVinci_Resolve_"$VERSION"_Linux.run" -i -y -n -C $REZ_BUILD_INSTALL_PATH
fi