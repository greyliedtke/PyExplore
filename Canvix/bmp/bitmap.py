from PIL import Image, ImageDraw

def create_checkered_bitmap():
    # Image size
    width, height = 8, 8

    # Create a new image with mode '1' (1-bit pixels, black and white)
    image = Image.new('1', (width, height))

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Draw a checkered pattern
    for x in range(width):
        for y in range(height):
            # Alternate between black and white based on position
            color = 0 if (x + y) % 2 == 0 else 1
            draw.point((x, y), fill=color)

    # Save the image
    image.save('checkered.bmp')

if __name__ == "__main__":
    create_checkered_bitmap()
