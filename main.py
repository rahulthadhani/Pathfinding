from headers import *

if __name__ == '__main__':
    FileArg = sys.argv[1] #The name of the image file to open
    WeightArg = sys.argv[2] #The name of the weights .txt file to open
    MovementArg = sys.argv[3] #The type of movement the agent can take (Four versus Eight) directions
    Start = (int(sys.argv[4]), int(sys.argv[5]))
    Destination = (int(sys.argv[6]), int(sys.argv[7]))

    InputImage = FileArg+".png"

    # Load terrain image
    TerrainImage = ps.OpenImage(InputImage)
    WIDTH, HEIGHT = TerrainImage.width,TerrainImage.height

    # Load weight file
    WeightFile = WeightArg + ".txt"
    ColorCosts = cf.LoadWeights(WeightFile)

    print(f"Terrain image: {WIDTH}x{HEIGHT}")
    print(f"Start: {Start}, Destination: {Destination}")
    print(f"Movement mode: {MovementArg}-way")

    # Run Dijkstra's Algorithm
    DijkstraPath, DijkstraCost, DijkstraDiscovered = ds.Dijkstra(
        TerrainImage, Start, Destination, ColorCosts, MovementArg
    )

    if DijkstraPath:
        print(f"Dijkstra - Path found! Cost: {DijkstraCost:.2f}")
        print(f"Dijkstra - Pixels discovered: {len(DijkstraDiscovered)}")

        # Create and save path image
        DijkstraPathImage = of.CreatePathImage(TerrainImage, DijkstraPath)
        DijkstraPathFilename = f"{FileArg.capitalize()}_{WeightArg.capitalize()}_{MovementArg}_DIJKSTRA_PATH_COST.png"
        ps.SaveImage(DijkstraPathImage, DijkstraPathFilename, "PNG")
        print(f"Saved: {DijkstraPathFilename}")

        # Create and save coverage image
        DijkstraCoverageImage = of.CreateCoverageImage(TerrainImage, DijkstraDiscovered)
        DijkstraCoverageFilename = f"{FileArg.capitalize()}_{WeightArg.capitalize()}_{MovementArg}_DIJKSTRA_COVERAGE.png"
        ps.SaveImage(DijkstraCoverageImage, DijkstraCoverageFilename, "PNG")
        print(f"Saved: {DijkstraCoverageFilename}")
    else:
        print("Dijkstra - No path found!")

    # Run A* Algorithm
    print("\nRunning A* Algorithm...")
    APath, ACost, ADiscovered = ast.AStar(
        TerrainImage, Start, Destination, ColorCosts, MovementArg
    )

    if APath:
        print(f"A* - Path found! Cost: {ACost:.2f}")
        print(f"A* - Pixels discovered: {len(ADiscovered)}")

        # Create and save path image
        APathImage = of.CreatePathImage(TerrainImage, APath)
        APathFilename = f"{FileArg.capitalize()}_{WeightArg.capitalize()}_{MovementArg}_ASTAR_PATH_COST.png"
        ps.SaveImage(APathImage, APathFilename, "PNG")
        print(f"Saved: {APathFilename}")

        # Create and save coverage image
        ACoverageImage = of.CreateCoverageImage(TerrainImage, ADiscovered)
        ACoverageFileName = f"{FileArg.capitalize()}_{WeightArg.capitalize()}_{MovementArg}ASTAR_COVERAGE.png"
        ps.SaveImage(ACoverageImage, ACoverageFileName, "PNG")
        print(f"Saved: {ACoverageFileName}")
    else:
        print("A* - No path found!")

