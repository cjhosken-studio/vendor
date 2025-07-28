@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building VSCode %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download VSCode if it doesn't exist
if not exist "vscode-%VERSION%.exe" (
    echo Downloading VSCode...
    curl -L https://update.code.visualstudio.com/%VERSION%/win32-x64-user/stable -o "vscode-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download VSCode
        exit /b 1
    )
)

:: Install VSCode
echo Installing VSCode...
"vscode-%VERSION%.exe" /VERYSILENT /NOCLOSEAPPLICATIONS /DIR=%REZ_BUILD_INSTALL_PATH%
if errorlevel 1 (
    echo ERROR: VSCode installation failed
    exit /b 1
)

echo Successfully installed VSCode %VERSION%