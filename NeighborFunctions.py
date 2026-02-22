from headers import *

def GetNeighbors(pixel, width, height, movementMode):
    # Get valid neighboring pixels based on movement mode
    x, y = pixel
    neighbors = []

    if movementMode == "4":
        # 4-way movement: up, down, left, right
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    else:  # movementMode == "8"
        # 8-way movement: includes diagonals
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check if neighbor is within bounds
        if 0 <= nx < width and 0 <= ny < height:
            neighbors.append((nx, ny))

    return neighbors

def IsDiagonal(current, neighbor):
    # Check if movement from current to neighbor is diagonal
    dx = abs(current[0] - neighbor[0])
    dy = abs(current[1] - neighbor[1])
    return dx == 1 and dy == 1