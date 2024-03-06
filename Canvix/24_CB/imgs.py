from PIL import Image, ImageEnhance

def resize_and_convert_to_indexed_bmp(input_file, output_file, size=(64, 64), brightness=.75):
    # Open the image
    with Image.open(input_file) as img:

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
        new_img.save(output_file, "BMP")

# Example usage
input_file = "Canvix/24_CB/in/spi.png"
output_file = "Canvix/24_CB/out/output_image.bmp"
resize_and_convert_to_indexed_bmp(input_file, output_file)
