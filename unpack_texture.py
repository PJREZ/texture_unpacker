import plistlib
from PIL import Image
import os
import sys

# 1. Catch missing arguments and show instructions
if len(sys.argv) != 3:
    print("Usage: python fix_sprites.py <file.plist> <file.png>")
    sys.exit(1)

# 2. Grab the inputs from the command line
plist_file = sys.argv[1]
png_file = sys.argv[2]

# 3. Create a dynamic output folder based on the plist name
folder_name = plist_file.replace('.plist', '') + "_unpacked"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

print(f"Unpacking {png_file} using data from {plist_file}...")

# Load the big image
atlas = Image.open(png_file)

# Load the data file
with open(plist_file, 'rb') as f:
    plist_data = plistlib.load(f)

# Go through every frame
for frame_name, data in plist_data['frames'].items():
    
    # Get the texture coordinates (where it is on the big sheet)
    tex_rect = data['textureRect'].replace('{', '').replace('}', '').split(',')
    tx, ty, tw, th = [int(val) for val in tex_rect]
    
    # Get the target size (the original size)
    source_size = data['spriteSourceSize'].replace('{', '').replace('}', '').split(',')
    sw, sh = [int(val) for val in source_size]
    
    # Get the placement coordinates (where it goes inside the box)
    color_rect = data['spriteColorRect'].replace('{', '').replace('}', '').split(',')
    cx, cy, cw, ch = [int(val) for val in color_rect]

    # Crop the sprite from the atlas
    sprite = atlas.crop((tx, ty, tx + tw, ty + th))
    
    # Create a new transparent image
    new_frame = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    
    # Paste the cropped sprite into the correct position
    new_frame.paste(sprite, (cx, cy))
    
    # Save it into the dynamic folder
    new_frame.save(f"{folder_name}/{frame_name}")

print(f"Success! Check the '{folder_name}' folder.")
