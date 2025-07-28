@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building Nuke %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%


if not exist "nuke-%VERSION%.zip" (
    echo Downloading Nuke...
    curl -L https://thefoundry.s3.amazonaws.com/products/nuke/releases/%VERSION%/Nuke%VERSION%-win-x86_64.zip -o nuke-%VERSION%.zip
    if errorlevel 1 (
        echo ERROR: Failed to download Nuke
        exit /b 1
    )
)

echo Installing Nuke...
tar -xz "nuke-%VERSION%.zip"

if errorlevel 1 (
    echo ERROR: Nuke installation failed
    exit /b 1
)

echo Successfully installed Nuke %VERSION%