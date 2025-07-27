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

installer = "Autodesk_Maya_2026_1_Update_ML_Linux_64bit"

build_command=f"""
if [ ! -f "{installer}.tgz" ]; then
    wget https://efulfillment.autodesk.com/NetSWDLD/prd/{version}/MAYA/A9AFE7E8-904B-3EEC-9689-0D2FD263FF90/{installer}.tgz
fi

if [ -f "{installer}.tgz" ]; then
    tar -xzf {installer}.tgz
    ./Setup --silent --install_dest $REZ_BUILD_INSTALL_PATH --noupdate
fi

"""

def commands():
    env.PATH.prepend(f"/usr/autodesk/maya{version}/bin")
    env.LD_LIBRARY_PATH.append(f"/usr/autodesk/maya{version}/lib")