Author: Rahul Thadhani
Description:

This is a pathfinder project where users are able to insert a terrain png file consisting
of pixels with different colors and different costs to find the fastest path to the destination
pixel provided. Each color has a specific cost specified in a Weights1.txt file. Users are able
to specify 4 way or 8 way movement. 4 way meaning up, down, left and right and 8 way meaning all
8 pixels surround the pixels being visited.The project contains helper functions in
Project1StarterCode.py, CostFunctions.py, NeighborFunctions.py, and OutputFunctions.py.
These functions are used to retrieve pixels colors,to find the cost of visiting a pixel,
to find all neighboring pixels (4 for 4 way movement and 8 for 8 way movement), and to create
and output of the terrain png showing all pixels that were checked and the final path produced
by the algorithm.

To perform the pathfinder algorithm we implemented Dijkstra's algorithm and an A* search
algorithm using Euclidean Distance (straight line distance) as the evaluation function.