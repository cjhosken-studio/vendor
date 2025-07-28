# Get version from parent directory name (e.g., "4.5")
VERSION=$(basename "$(dirname "$0")")

# Extract major and minor versions (e.g., "4" and "5")
MAJOR_VERSION="${VERSION%%.*}"  # Everything before the first dot
MINOR_VERSION="${VERSION#*.}"   # Everything after the first dot

PYTHON_VERSION="3.11"

# Download Blender (using full version)
wget "https://download.blender.org/release/Blender${MAJOR_VERSION}.${MINOR_VERSION}/blender-${VERSION}-linux-x64.tar.xz"
tar -xf "blender-${VERSION}-linux-x64.tar.xz" -C "$REZ_BUILD_INSTALL_PATH" --strip-components=1

# Install Python deps (using full version)
"$REZ_BUILD_INSTALL_PATH/${VERSION}/python/bin/python$PYTHON_VERSION" -m pip install PySide6 numpy

# Splash screen setup (using full version)
mkdir -p "$REZ_BUILD_INSTALL_PATH/${VERSION}/scripts/startup/bl_app_templates_system/blender"
cp -r ../splash/* "$REZ_BUILD_INSTALL_PATH/${VERSION}/scripts/startup/bl_app_templates_system/blender"