TextureUnpacker "Frame" error for plist3 fix
updated the script to use the modern "Format 3" vocabulary
========================
Usage Example: **python unpack_texture.py NAME.plist NAME.png**

# Overview
Use this script to unpack **.png** sprites from the sprite atlas (providing a **.plist** or **.json** data file and a **.png** file) packed by [TexturePacker](http://www.codeandweb.com/texturepacker/).

# Dependencies
  - [Python](http://www.python.org)
  - [Pillow (PIL fork)](https://github.com/python-pillow/Pillow) 

# Usage
	
	$ python unpack_texture.py <filename without extension or folder path> <format [plist|json|cocos]>
	
## filename

- Filename of the sprite atlas image and data file without extensions.

## format 

*optional*

- Data file format. Valid values are **plist** and **json**. If omitted **plist** format is assumed.
