name = "substance_designer"

description = \
    """
    Substance 3D Designer is primarily a 3D design software that generates textures from procedural patterns inside node-based graphs.
    """

authors = [
    "Adobe"
]

def commands():
    designer_root = "C:/Program Files/Adobe/Adobe Substance 3D Designer"
    env.PATH.prepend(designer_root)
    env.SUBSTANCE_DESIGNER_ROOT.set(designer_root)
    designer_exe = f'"{designer_root}/Adobe Substance 3D Designer.exe"'
    alias("designer", f'& {designer_exe} $args')
    
build_command = ""