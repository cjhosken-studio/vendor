@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building MiniConda %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download MiniConda if it doesn't exist
if not exist "miniconda-%VERSION%.exe" (
    echo Downloading MiniConda...
    curl -L https://repo.anaconda.com/miniconda/Miniconda3-py313_%VERSION%-1-Windows-x86_64.exe -o "miniconda-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download MiniConda
        exit /b 1
    )
)

:: Install MiniConda
echo Installing MiniConda...
"miniconda-%VERSION%.exe" /S /H %REZ_BUILD_INSTALL_PATH%
if errorlevel 1 (
    echo ERROR: MiniConda installation failed
    exit /b 1
)

echo Successfully installed MiniConda %VERSION%