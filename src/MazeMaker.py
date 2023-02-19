import random

def maze_return():
    # Set the size of the maze
    width = 17
    height = 17

    # Initialize the maze as a 2D array of walls
    maze = [[0] * width for _ in range(height)]

    # Set the starting point
    start = (1, 1)

    # Set the endpoint
    end = (width - 2, height - 2)

    # Define a function to check if a cell is a valid location in the maze
    def is_valid(x, y):
        return x >= 0 and y >= 0 and x < width and y < height

    # Define a function to get the neighbors of a cell
    def get_neighbors(x, y):
        neighbors = []
        if is_valid(x-2, y) and maze[y][x-2] == 0:
            neighbors.append((x-2, y))
        if is_valid(x+2, y) and maze[y][x+2] == 0:
            neighbors.append((x+2, y))
        if is_valid(x, y-2) and maze[y-2][x] == 0:
            neighbors.append((x, y-2))
        if is_valid(x, y+2) and maze[y+2][x] == 0:
            neighbors.append((x, y+2))
        return neighbors

    # Define the depth-first search algorithm to generate the maze
    def dfs(x, y):
        maze[y][x] = 1
        neighbors = get_neighbors(x, y)
        random.shuffle(neighbors)
        for (nx, ny) in neighbors:
            if maze[ny][nx] == 0:
                maze[(y + ny) // 2][(x + nx) // 2] = 1
                dfs(nx, ny)

    # Generate the maze
    dfs(start[0], start[1])

    # Set the start and end points to be open spaces
    maze[start[1]][start[0]] = 1
    maze[end[1]][end[0]] = 1

    return maze
