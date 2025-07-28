@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building Maya %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Davinci Resolve if it doesn't exist
if not exist "maya-%VERSION%.exe" (
    echo Downloading Maya...
    curl -L https://upload1.delivery.autodesk.com/PORTAL_DownloadPackage503306580336969.exe?response-content-disposition=attachment%3B%20filename%20%3D%22Create_Installer_MAYA_2026_English_WIN64.exe -o "maya-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download Maya
        exit /b 1
    )
)

:: Install maya
echo Installing Maya...
"maya-%VERSION%.exe"

if errorlevel 1 (
    echo ERROR: Maya installation failed
    exit /b 1
)

echo Successfully installed Maya %VERSION%