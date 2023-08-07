#!/usr/bin/env python
"""
This script creates PNGs compatible as extension icons out of SVG files using Cairo Graphics library, it should work by default on most Linux distros and would require Cairo installation for it to work on Windows
"""

import cairosvg
import os

def convert_svg_to_png(input_file, output_directory):
    sizes = [16, 32, 48, 128]
    
    os.makedirs(output_directory, exist_ok=True)
    
    for size in sizes:
        output_filename = os.path.join(output_directory, f"icon-{size}.png")
        cairosvg.svg2png(url=input_file, write_to=output_filename, output_width=size, output_height=size)

if __name__ == "__main__":
    input_file = "file.svg"
    output_directory = "images"
    
    convert_svg_to_png(input_file, output_directory)