@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Extract major and minor version (e.g., from "4.5.0" get "4.5")
for /f "tokens=1,2 delims=." %%a in ("%VERSION%") do (
    set "MAJOR_MINOR=%%a.%%b"
)

:: Debug output
echo Building Blender %VERSION% for Windows...
echo Major.Minor version: %MAJOR_MINOR%
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Blender if it doesn't exist
if not exist "blender-%VERSION%.zip" (
    echo Downloading Blender...
    curl -L https://download.blender.org/release/Blender%MAJOR_MINOR%/blender-%VERSION%-windows-x64.zip -o "blender-%VERSION%.zip"
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
mkdir "%REZ_BUILD_INSTALL_PATH%\%MAJOR_MINOR%\scripts\startup\bl_app_templates_system\blender" >nul 2>&1

REM Copy splash files to the target directory
xcopy /E /I "..\splash\*" "%REZ_BUILD_INSTALL_PATH%\%MAJOR_MINOR%\scripts\startup\bl_app_templates_system\blender\"

echo Successfully installed Blender %VERSION%