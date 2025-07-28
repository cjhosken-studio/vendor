@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

set INSTALL_LINK=https://thefoundry.s3.amazonaws.com/products/mari/releases/7.1v2/Mari7.1v2-win-x86-release-64.zip?AWSAccessKeyId=AKIASB3GJ7KM7A6GWLWU&Expires=1753743163&response-content-disposition=attachment%3B%20filename%20%3D%20Mari7.1v2-win-x86-release-64.zip&Signature=ceuQeDtIxKWJJTMRZhfJsJNXFis%3D

:: Debug output
echo Building Mari %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%


if not exist "mari-%VERSION%.zip" (
    echo Downloading Mari...
    curl -L %INSTALL_LINK% -o mari-%VERSION%.zip
    if errorlevel 1 (
        echo ERROR: Failed to download Mari
        exit /b 1
    )
)

echo Installing Mari...
tar -xz "mari-%VERSION%.zip"

if errorlevel 1 (
    echo ERROR: Mari installation failed
    exit /b 1
)

echo Successfully installed Mari %VERSION%