@echo off

:: Get version from parent folder name
for %%A in ("%~dp0.") do set "VERSION=%%~nxA"

:: Debug output
echo Building Houdini %VERSION% for Windows...
echo REZ_BUILD_INSTALL_PATH: %REZ_BUILD_INSTALL_PATH%

:: Download Houdini if it doesn't exist
if not exist "houdini-%VERSION%.exe" (
    echo Downloading Houdini...
    curl -L https://d199n7he4uszw5.cloudfront.net/download/download-build/134465/cdn/?Expires=1753749665&Signature=uxABQ1kyVLmIvISlWGyt3IOzvu6psu6x08S50QznOaKX-za~7LhnPncfBjQymSsOnTYuKeOynm3ZL62Ev5pX96c628BU3u-O3sJNxcH29ABnEwjNgNdhJl5yzbK0hnVaQyqWVj9sobaXol9yUsOH5aWkGTruWfMTTtZvE9fuol0hvo6a6uNTzHnBycplbUQhI3c5466F1UVhq255IHOE2jU2uS7EnCh9YLVlp-i3bo-TRdIxygUN7Eb-WDk9bcAvaFbw~LnqHMyC1jI2pleaYX~LprivJ94WmvVrUpAfzMELbzY6dOQew7wrV59SidIbTnLbP4FupsHcnOjE0cjpkA__&Key-Pair-Id=APKAITRNKY64UW6MKIWQ -o "houdini-%VERSION%.exe"
    if errorlevel 1 (
        echo ERROR: Failed to download Houdini
        exit /b 1
    )
)

:: Install houdini
echo Installing Houdini...
"houdini-%VERSION%.exe"
if errorlevel 1 (
    echo ERROR: Houdini installation failed
    exit /b 1
)

echo Successfully installed Houdini %VERSION%