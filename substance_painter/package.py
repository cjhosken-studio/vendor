name = "substance_painter"

description = \
    """
    Substance Painter is a 3D painting software, primarily used for creating and texturing 3D models. 
    It's known for its non-destructive workflow, allowing for edits and resolution changes without data loss, and its ability to create realistic, physically-based rendering (PBR) materials.
    """

authors = [
    "Adobe"
]

def commands():
    painter_root = "C:/Program Files/Adobe/Adobe Substance 3D Painter"
    env.PATH.prepend(painter_root)
    env.SUBSTANCE_PAINTER_ROOT.set(painter_root)
    env.PAINTER_CMD.set(f'"{painter_root}/Adobe Substance 3D Painter.exe"')
    painter_exe = f'"{painter_root}/Adobe Substance 3D Painter.exe"'
    alias("painter", f'& {painter_exe} $args')

build_command = ""