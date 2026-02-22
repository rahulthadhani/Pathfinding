from headers import *

def Dijkstra(terrainImage, start, destination, colorCosts, movementMode):
    width, height = terrainImage.width, terrainImage.height

    # Priority queue: (cost, pixel)
    pq = [(0, start)]

    # Track costs to reach each pixel
    costs = {start: 0}

    # Track parent for path reconstruction
    parent = {start: None}

    # Track all discovered pixels
    discovered = set([start])

    while pq:
        currentCost, current = heapq.heappop(pq)

        # If we've reached the destination, reconstruct path
        if current == destination:
            path = []
            node = destination
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, currentCost, discovered

        # Skip if we've already processed this with a better cost
        if currentCost > costs.get(current, float('inf')):
            continue

        # Explore neighbors
        neighbors = nf.GetNeighbors(current, width, height, movementMode)
        for neighbor in neighbors:
            # Calculate cost to reach this neighbor
            pixelCost = cf.GetPixelCost(terrainImage, neighbor, colorCosts)

            # Diagonal movement costs sqrt(2) times the pixel cost
            if nf.IsDiagonal(current, neighbor):
                moveCost = math.sqrt(2) * pixelCost
            else:
                moveCost = pixelCost

            newCost = currentCost + moveCost

            # If we found a better path to this neighbor
            if newCost < costs.get(neighbor, float('inf')):
                costs[neighbor] = newCost
                parent[neighbor] = current
                discovered.add(neighbor)
                heapq.heappush(pq, (newCost, neighbor))

    # No path found
    return [], float('inf'), discovered