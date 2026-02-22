from headers import *

def LoadWeights(WeightFile):
    # Load color-to-cost mappings from weight file
    colorCost = {}
    try:
        with open(WeightFile, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    r, g, b, cost = int(parts[0]), int(parts[1]), int(parts[2]), float(parts[3])
                    colorCost[(r, g, b)] = cost
    except FileNotFoundError:
        print(f"Warning: Weight file {WeightFile} not found. Using default costs.")
    return colorCost

def GetPixelCost(image, pixel, colorCost):
    # Get the cost of entering a pixel based on its color
    color = ps.GetRGB(image, pixel)
    return colorCost.get(color, 1)  # Default cost is 1
