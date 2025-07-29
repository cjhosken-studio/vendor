# Vendor
This repository contains rez build scripts for vendor softwares.

## General Notes

- Adobe Substance Painter and Adobe Substance Designer cannot be built on linux.


## Usage
software is built by diving into the package.py directory and running `rez build -i`.

Some software may prompt you to do extra actions, as not all tools can be installed automatically (eg: Houdini)

## Windows
At the moment, windows is (sort of) supported. Admin should install software into their normal locations, and the rez build scripts should find their locations.

*Make sure that the version you install matches the version in the rez build.*

Some software such as:
    - Blender

can be built using `rez build -i` for windows.

Since Windows doesn't usually allow multiple installs of the same software, some of the build scripts will find the **main/most recent install** of the tool:
    - DaVinci Resolve
    - Miniconda
    - VSCode
    - Substance Painter
    - Substance Designer

## Maintenance
This repository is maintained by [Christopher Hosken](cjhosken.github.io)