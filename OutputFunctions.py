from headers import *

def CreatePathImage(TerrainImage, path):
    # Create image with path marked in red
    outputImage = TerrainImage.copy()
    for pixel in path:
        ps.SetRGB(outputImage, pixel, (255, 0, 0))
    return outputImage

def CreateCoverageImage(TerrainImage, discovered):
    # Create image with discovered pixels marked in black
    outputImage = TerrainImage.copy()
    for pixel in discovered:
        ps.SetRGB(outputImage, pixel, (0, 0, 0))
    return outputImage