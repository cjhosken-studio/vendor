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

requires = [
]

build_command=""

def commands():
    env.PATH.prepend(f"/usr/autodesk/maya{version}/bin")
    env.LD_LIBRARY_PATH.append(f"/usr/autodesk/maya{version}/lib")