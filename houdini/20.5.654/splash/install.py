import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.environ.get("REZ_BUILD_INSTALL_PATH")

if not output_dir:
    raise ValueError("Environment variable 'REZ_BUILD_INSTALL_PATH' is not set!")

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(script_dir):
    if filename.lower().endswith('.png'):
        input_path = os.path.join(script_dir, filename)
        output_filename = os.path.splitext(filename)[0] + ".pic"
        output_path = os.path.join(output_dir, output_filename)

        # Use Houdini's hiconvert
        try:
            subprocess.run(["hiconvert", input_path, output_path], check=True)
            print(f"Converted: {filename} → {output_filename}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {filename}: {e}")