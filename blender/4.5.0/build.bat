@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building Blender %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Blender if it doesn't exist
if not exist "blender-%VERSION%.zip" (
    echo Downloading Blender...
    curl -L https://download.blender.org/release/Blender4.5/blender-%VERSION%-windows-x64.zip -o "blender-%VERSION%.zip"
    if errorlevel 1 (
        echo ERROR: Failed to download Blender
        exit /b 1
    )
)

:: Install Blender
echo Installing Blender...
tar -xf "blender-%VERSION%.zip" --strip-components=1 -C "%REZ_BUILD_INSTALL_PATH%"
if errorlevel 1 (
    echo ERROR: Blender installation failed
    exit /b 1
)

echo Setting up Splash Screens...
REM Create the target directory structure
mkdir "%REZ_BUILD_INSTALL_PATH%\4.5\scripts\startup\bl_app_templates_system\blender" >nul 2>&1

REM Copy splash files to the target directory
xcopy /E /I "..\splash\*" "%REZ_BUILD_INSTALL_PATH%\4.5\scripts\startup\bl_app_templates_system\blender\"

echo Successfully installed Blender %VERSION%
