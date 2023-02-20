import random

def maze_return(n, m):
    # Create a maze of all walls
    maze = [[0 for x in range(m)] for y in range(n)]

    # Set the starting position to a random cell on the left edge
    start_x = 0
    start_y = random.randint(0, n-1)
    maze[start_y][start_x] = 1

    # Set the goal position to a random cell on the right edge
    goal_x = m-1
    goal_y = random.randint(0, n-1)
    maze[goal_y][goal_x] = 1

    # Generate a random path from the starting position to the goal position
    current_x = start_x
    current_y = start_y
    while current_x != goal_x or current_y != goal_y:
        # Determine which direction to move in (up, down, left, or right)
        direction = random.randint(0, 3)
        if direction == 0 and current_y > 0 and maze[current_y-1][current_x] == 0:
            # Move up
            current_y -= 1
            maze[current_y][current_x] = 1
        elif direction == 1 and current_y < n-1 and maze[current_y+1][current_x] == 0:
            # Move down
            current_y += 1
            maze[current_y][current_x] = 1
        elif direction == 2 and current_x > 0 and maze[current_y][current_x-1] == 0:
            # Move left
            current_x -= 1
            maze[current_y][current_x] = 1
        elif direction == 3 and current_x < m-1 and maze[current_y][current_x+1] == 0:
            # Move right
            current_x += 1
            maze[current_y][current_x] = 1

    return maze
