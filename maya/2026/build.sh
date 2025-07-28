VERSION=$(basename "$(dirname "$0")")

INSTALLER="Autodesk_Maya_"$VERSION"_1_Update_ML_Linux_64bit"

if [ ! -f "$INSTALLER.tgz" ]; then
    wget https://efulfillment.autodesk.com/NetSWDLD/prd/$INSTALLER/MAYA/A9AFE7E8-904B-3EEC-9689-0D2FD263FF90/{installer}.tgz
fi

if [ -f "$INSTALLER.tgz" ]; then
    tar -xzf $INSTALLER.tgz
    ./Setup --silent --install_dest $REZ_BUILD_INSTALL_PATH --noupdate
fi