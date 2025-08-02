# Get version from parent directory name (e.g., "4.5" or "4.5.2")
VERSION=$(basename "$(dirname "$0")")

# Extract major and minor versions (strictly first and second numbers only)
MAJOR_VERSION="${VERSION%%.*}"  # Extracts the major version (first number)
MINOR_VERSION="${VERSION#*.}"   # Get everything after first dot
MINOR_VERSION="${MINOR_VERSION%%.*}"  # Then take only before next dot

PYTHON_VERSION="3.11"

# Download Blender (using full version)
wget "https://download.blender.org/release/Blender${MAJOR_VERSION}.${MINOR_VERSION}/blender-${VERSION}-linux-x64.tar.xz"
tar -xf "blender-${VERSION}-linux-x64.tar.xz" -C "$REZ_BUILD_INSTALL_PATH" --strip-components=1

# Splash screen setup (using full version)
mkdir -p "$REZ_BUILD_INSTALL_PATH/${MAJOR_VERSION}.${MINOR_VERSION}/scripts/startup/bl_app_templates_system/blender"
cp -r ../splash/* "$REZ_BUILD_INSTALL_PATH/${MAJOR_VERSION}.${MINOR_VERSION}/scripts/startup/bl_app_templates_system/blender"