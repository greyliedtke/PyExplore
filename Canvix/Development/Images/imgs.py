"""
script to resize and convert images to indexed bmp
Also to resize and convert to rgb matrix
"""

import os, sys
from PIL import Image, ImageEnhance
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# ------------------------------------------------------
# RGB Conversion
def png_to_rgb(fname, size=(16,16)):
    # resize to matrix size and create rgb and pixel array
    img_in = Image.open(f"PNG/{fname}")
    fname = fname.split('.')[0]
    img_o = img_in.resize(size)
    img_o = img_o.convert("RGB")

    p_i = []
    for y in range(size[1]):
        for x in range(size[0]):
            # Get RGB color of the pixel
            rgb = list(img_o.getpixel((x, 15-y)))
            p_i.append([[x,y],rgb])

    with open(f"RGB/{fname}.py", 'w') as file:
        file.write(fname + " = [\n")
        for row in p_i:
            file.write("    [" + ", ".join(map(str, row)) + "],\n")
        file.write("]\n")
# ------------------------------------------------------

# ------------------------------------------------------
# Bitmap conversion 64x64
def bitmap_conversion(fname, size=(64, 64), brightness=.75):
    # Open the image
    with Image.open(f"PNG/{fname}") as img:
        fname = fname.split('.')[0]
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)
        # Resize the image to fit within the specified size without distorting
        img.thumbnail(size)
        # Create a new blank image with the desired size
        new_img = Image.new("RGB", size, color="white")
        # Paste the resized image onto the blank image to center it
        position = ((size[0] - img.width) // 2, (size[1] - img.height) // 2)
        new_img.paste(img, position)
        # Convert to indexed mode (using the default palette)
        new_img = new_img.convert("P")
        # Save as BMP
        new_img.save(f"BMP/{fname}.bmp", "BMP")
# ------------------------------------------------------

# ------------------------------------------------------
# Running Script
input_file = "mn.jpg"
bitmap_conversion(input_file, brightness=1)
png_to_rgb(input_file)
# ------------------------------------------------------
