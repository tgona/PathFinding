import pygame
from MazeMaker import *
from tkinter import *
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Define the maze as a 2D list of 0's and 1's, where 0 represents a wall and 1 represents a passage
maze = maze_return()
# Define the size of the maze cells and the screen
cell_size = 50
screen_width = len(maze[0]) * cell_size
screen_height = len(maze) * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Maze Game")

# Initialize the font
font_path = pygame.font.match_font("arial")
font = pygame.font.Font(font_path, 36)

# Define the colors for the walls, passages, point, and goal
wall_color = (0, 0, 0)
passage_color = (255, 255, 255)
point_color = (255, 0, 0)
goal_color = (0, 255, 0)

# Define the starting position of the point
point_pos = [1, 1]

# Define the goal position of the point
goal_pos = [len(maze)-2, len(maze)-2]

# Define the clock to control the frame rate
clock = pygame.time.Clock()

game_over = False
# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            # Move the point based on arrow keys
            if event.key == pygame.K_UP and maze[point_pos[1]-1][point_pos[0]] == 1:
                point_pos[1] -= 1
            elif event.key == pygame.K_DOWN and maze[point_pos[1]+1][point_pos[0]] == 1:
                point_pos[1] += 1
            elif event.key == pygame.K_LEFT and maze[point_pos[1]][point_pos[0]-1] == 1:
                point_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and maze[point_pos[1]][point_pos[0]+1] == 1:
                point_pos[0] += 1
            elif event.key == pygame.K_ESCAPE:
                game_over = True
                pygame.quit()
                quit()

    # Clear the screen
    screen.fill((255, 255, 255))

        # Draw the maze
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 0:
                pygame.draw.rect(screen, wall_color, (x*cell_size, y*cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, passage_color, (x*cell_size, y*cell_size, cell_size, cell_size))

    # Draw the point
    pygame.draw.rect(screen, point_color, (point_pos[0]*cell_size, point_pos[1]*cell_size, cell_size, cell_size))

    # Draw the goal
    pygame.draw.rect(screen, goal_color, (goal_pos[0]*cell_size, goal_pos[1]*cell_size, cell_size, cell_size))

    if point_pos == goal_pos:
        # Create the surface to display the message on
        message_surface = font.render("Congratulations! You scored over 100 points!", True, (255, 255, 255), (0, 0, 0))
        message_rect = message_surface.get_rect(center=(screen_width/2, screen_height/2))

        # Display the message on the main window
        screen.blit(message_surface, message_rect)
        
    # Update the screen
    pygame.display.update()
    


    # Control the frame rate
    clock.tick(60)
