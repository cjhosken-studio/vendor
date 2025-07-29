name = "maya"

version = "2026"

authors = [
    "Autodesk"
]

description = \
    """
    Maya 3D is a professional software application developed by Autodesk for creating 3D computer graphics. 
    It's widely used in the film, television, video game, and visual effects industries to create 3D models, animations, visual effects, and simulations.
    """

tools = [
    "maya",
]

def commands():
    import platform

    if platform.system() == "Windows":
        maya_root = f"C:/Program Files/Autodesk/Maya{version}"
        env.PATH.prepend(f"{maya_root}/bin")
    else:
        env.PATH.prepend(f"/usr/autodesk/maya{version}/bin")
        env.LD_LIBRARY_PATH.append(f"/usr/autodesk/maya{version}/lib")

import platform

if platform.system() == "Windows":
    build_command = ""
else:
    build_command = "{root}/build.sh"