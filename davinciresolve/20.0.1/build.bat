@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building Davinci Resolve %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Davinci Resolve if it doesn't exist
if not exist "resolve-%VERSION%.zip" (
    echo Downloading Davinci Resolve...
    curl -L https://swr.cloud.blackmagicdesign.com/DaVinciResolve/v%VERSION%/DaVinci_Resolve_%VERSION%_Windows.zip?verify=1753734011-Z3zOOHXyem4ztR3WxIL41lKzXRMwsGReOXPDAMnBSaA%3D -o "resolve-%VERSION%.zip"
    if errorlevel 1 (
        echo ERROR: Failed to download Davinci Resolve
        exit /b 1
    )
)

:: Install Davinci Resolve
echo Installing Davinci Resolve...
tar -xz "resolve-%VERSION%.zip"

::/VERYSILENT /NOCLOSEAPPLICATIONS /DIR=%REZ_BUILD_INSTALL_PATH%
if errorlevel 1 (
    echo ERROR: Davinci Resolve installation failed
    exit /b 1
)

echo Successfully installed Davinci Resolve %VERSION%