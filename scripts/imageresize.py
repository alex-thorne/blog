import os
import sys
import subprocess
from PIL import Image

# This script resizes an image to 50%, 25%, and 12.5% of the original size.
# Usage: python imageresize.py <filename>
# stores the resized images in the same directory as the original image.

def resize_image(filename):
    # Get the directory and the base name of the file
    directory, base_name = os.path.split(filename)
    name, ext = os.path.splitext(base_name)
    
    # Define the resize percentages and the new filenames
    sizes = {
        '@50': 50,
        '@25': 25,
        '@12.5': 12.5
    }
    
    # List to store the output information
    output_info = []

    # Add original image info
    with Image.open(filename) as img:
        width, height = img.size
        original_info = {
            'filename': filename,
            'width': width,
            'height': height
        }
        output_info.append(original_info)
    
    # Iterate through each size and resize the image
    for suffix, percentage in sizes.items():
        new_filename = os.path.join(directory, f"{name}{suffix}{ext}")
        resize_command = [
            'convert', filename,
            '-resize', f'{percentage}%',
            new_filename
        ]
        
        # Run the ImageMagick convert command
        subprocess.run(resize_command, check=True)
        
        # Get the dimensions of the new image
        with Image.open(new_filename) as img:
            width, height = img.size
            new_info = {
                'filename': new_filename,
                'width': width,
                'height': height
            }
            output_info.append(new_info)

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