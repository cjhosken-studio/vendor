VERSION=$(basename "$(dirname "$0")")

wget https://update.code.visualstudio.com/$VERSION/linux-x64/stable -O vscode.tgz

if [ -f vscode.tgz ]; then
    tar -xzf vscode.tgz -C $REZ_BUILD_INSTALL_PATH --strip-components=1
fi
