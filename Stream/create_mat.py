from PIL import Image

# Create a 16x16 RGB image with a cool pattern
image = Image.new('RGB', (16, 16))

# Define your colors using RGB values
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Create a pattern using these colors
pixels = [
    red, blue, green, yellow,
    yellow, red, blue, green,
    green, yellow, red, blue,
    blue, green, yellow, red,
    red, blue, green, yellow,
    yellow, red, blue, green,
    green, yellow, red, blue,
    blue, green, yellow, red,
    red, blue, green, yellow,
    yellow, red, blue, green,
    green, yellow, red, blue,
    blue, green, yellow, red,
    red, blue, green, yellow,
    yellow, red, blue, green,
    green, yellow, red, blue,
    blue, green, yellow, red
]

# Put the pixels in the image
image.putdata(pixels)

# Display or save the image
image.show()
# image.save("cool_image.png")  # Save the image to a file
