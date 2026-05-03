#!/usr/bin/env python3
import os
import sys
import subprocess

# This script resizes an image to 50%, 25%, and 12.5% of the original size.
# Usage: python imageresize.py <filename>
# stores the resized images in the same directory as the original image.

def get_dimensions(filename):
    result = subprocess.run(
        ['magick', 'identify', '-format', '%w %h', filename],
        check=True, capture_output=True, text=True
    )
    width, height = result.stdout.strip().split()
    return int(width), int(height)

def resize_image(filename):
    # Get the directory and the base name of the file
    directory, base_name = os.path.split(filename)
    name, ext = os.path.splitext(base_name)

    # Define the resize percentages and the new filenames
    sizes = {
        '@0,5x': 50,
        '@0,25x': 25,
        '@0,125x': 12.5
    }

    # List to store the output information
    output_info = []

    # Add original image info
    width, height = get_dimensions(filename)
    output_info.append({
        'filename': filename,
        'width': width,
        'height': height
    })

    # Iterate through each size and resize the image
    for suffix, percentage in sizes.items():
        new_filename = os.path.join(directory, f"{name}{suffix}{ext}")
        resize_command = [
            'magick', filename,
            '-resize', f'{percentage}%',
            new_filename
        ]

        # Run the ImageMagick convert command
        subprocess.run(resize_command, check=True)

        # Get the dimensions of the new image
        width, height = get_dimensions(new_filename)
        output_info.append({
            'filename': new_filename,
            'width': width,
            'height': height
        })

    # Print the output information
    for info in output_info:
        print(f"Filename: {info['filename']}, Width: {info['width']}, Height: {info['height']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resize_images.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    
    resize_image(filename)