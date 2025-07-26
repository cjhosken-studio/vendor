name = "houdini"

version = "20.5.654"

authors = [
    "SideFX"
]

description = \
    """
    Houdini is a 3D animation and visual effects (VFX) software renowned for its procedural workflow, which allows artists to create dynamic and complex simulations and effects in film, television, and games.
    """

tools = [
    "houdini",
    "hython"
]

requires = [
]

installer = "houdini-{version}-linux_x86_64_gcc11.2"

build_command=f"""

if [ ! -f {installer}.tar.gz ]; then
    wget https://d199n7he4uszw5.cloudfront.net/download/download-build/134413/cdn/?Expires=1753579650&Signature=6GjJoproJDAW4wkdP6CgEAxuT1f-w4wQFLn8WXakj7GCYI5diAvkD5FRCFoSi9otcth0JGdZJzhPJk24BIyYdjz3FBUmRnrNGK-GCsNXKjUgLaP-yFKfXaStRRs3amveU2tBCKOpt2tW2DJZPhNL6PfW-yuFFLWg9350B8XN6C71HRncUnd4ydZFH-IksjYNA5vSTphcl80p5wog1OLeytqsrpZd8gJwSJLp1H2QE5wR9EdiQj0DZQFzQGSK39Xbe72UyJkfRpOLMgK~ISY~-LzTFWI7ncmCxLHWs1ZyiqT~7QhOEC~Kt7ZxC~scltIomfLInUOXbTWiq3irxwosew__&Key-Pair-Id=APKAITRNKY64UW6MKIWQ
fi
    
if [ -f {installer}.tar.gz ] ; then
    tar -xzf {installer}.tar.gz
    {installer}/houdini.install --install-houdini --install-sidefxlabs --sidefxlabs-dir $REZ_BUILD_INSTALL_PATH/SideFXLabs --install-menus --no-root-check $REZ_BUILD_INSTALL_PATH
fi

# splash stuffs
PATH=PATH:$REZ_BUILD_INSTALL_PATH/bin
python3 ../splash/install.py
"""

def commands():
    env.PATH.append("{root}/bin:{root}/python/bin")

    env.LD_LIBRARY_PATH.append("{root}/dsolib")

    env.HFS.set("{root}")
    env.HOUDINI_ROOT.set("{root}")

def post_commands():
    command("cd $HOUDINI_ROOT; source ./houdini_setup; cd -")