from headers import *

def EuclideanDistance(pixel1, pixel2):
    # Calculate Euclidean distance between two pixels
    return math.sqrt((pixel1[0] - pixel2[0])**2 + (pixel1[1] - pixel2[1])**2)


def AStar(terrainImage, start, destination, colorCosts, movementMode):

    # A* Algorithm for finding optimal path using Euclidean distance heuristic
    # Returns: (path, total_cost, discovered_pixels)

    width, height = terrainImage.width, terrainImage.height

    # Priority queue: (FScore, pixel)
    # FScore = GScore + HScore
    HStart = EuclideanDistance(start, destination)
    pq = [(HStart, start)]

    # Track actual cost from start (GScore)
    GScores = {start: 0}

    # Track parent for path reconstruction
    parent = {start: None}

    # Track all discovered pixels
    discovered = set([start])

    while pq:
        FScore, current = heapq.heappop(pq)

        # If we've reached the destination, reconstruct path
        if current == destination:
            path = []
            node = destination
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, GScores[current], discovered

        # Get current GScore
        GCurrent = GScores.get(current, float('inf'))

        # Skip if we've already processed this with a better GScore
        if GCurrent + EuclideanDistance(current, destination) > FScore:
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

            GNeighbor = GCurrent + moveCost

            # If we found a better path to this neighbor
            if GNeighbor < GScores.get(neighbor, float('inf')):
                GScores[neighbor] = GNeighbor
                parent[neighbor] = current
                discovered.add(neighbor)

                # Calculate FScore for priority queue
                HScore = EuclideanDistance(neighbor, destination)
                FScore = GNeighbor + HScore
                heapq.heappush(pq, (FScore, neighbor))

    # No path found
    return [], float('inf'), discovered