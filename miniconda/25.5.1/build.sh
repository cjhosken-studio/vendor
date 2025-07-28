VERSION=$(basename "$(dirname "$0")")

PYTHON_VERSION="313"

INSTALLER="Miniconda3-py"$PYTHON_VERSION"_"$VERSION"-1-Linux-x86_64.sh"

wget https://repo.anaconda.com/miniconda/$INSTALLER
chmod +x "./$INSTALLER"
"./$INSTALLER" -b -f -p $REZ_BUILD_INSTALL_PATH