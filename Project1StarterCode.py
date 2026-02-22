from headers import *

# =====IMAGE HELPERS=====
# Aside: Why do this when the functions are all just one liners?
# Consider switching to a different image library (opencv), representation, etc.
# This cleans up the code a bit by leaving the logic of the search algorithms independent of the specific image package.
# If we were to change, we would just need to update logic here once

def SetRGB(image, pixel_coordinate, color):
    image.putpixel(pixel_coordinate, color)

def GetRGB(image, pixel_coordinate):
    return image.getpixel(pixel_coordinate)

def SaveImage(image, filename, extension):
    image.save(filename, extension)

def OpenImage(filename):
    return  Image.open(filename)
