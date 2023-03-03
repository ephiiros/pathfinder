import pygame
from typing import *
from pathfinder import PathFinder
from pathfinder import Node

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

window_length = 600
cell_length = 50
cell_num = int(window_length/cell_length)
game_grid = [[0] * cell_num for _ in range(cell_num)]

# walls 
walls = [(5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9)]
for wall in walls:
    game_grid[wall[0]][wall[1]] = 1

# goal
goal = (cell_num-1, cell_num-1)
game_grid[cell_num-1][cell_num-1] = 2

# start
x_coord = 0
y_coord = 0
game_grid[x_coord][y_coord] = 3
 
pygame.init()
pygame.display.set_caption('pathfinding')
dis = pygame.display.set_mode((window_length+200, window_length))
game_over = False

font = pygame.font.Font('freesansbold.ttf', 16)

algo = font.render("algo : breadth first", True, BLACK)
neighbour = font.render("neighbours q: (4) 8", True, BLACK)


clock = pygame.time.Clock()

mouse_down = False

pf = PathFinder(4)
path: Node = Node((0,0),None)
path_start: Node = Node((0,0),None)
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                mouse_down = True
                mouse_x, mouse_y = event.pos
                new_x = mouse_x // cell_length
                new_y = mouse_y // cell_length

                if game_grid[new_x][new_y] == 0:
                    # player moves
                    game_grid[x_coord][y_coord] = 0
                    x_coord = new_x
                    y_coord = new_y
                    game_grid[x_coord][y_coord] = 3

                    path_start = pf.find_path(game_grid, (x_coord, y_coord))
            if event.button == 3:
                mouse_x, mouse_y = event.pos
                new_goal_x = mouse_x // cell_length
                new_goal_y = mouse_y // cell_length

                if game_grid[new_goal_x][new_goal_y] == 0:

                    game_grid[goal[0]][goal[1]] = 0
                    goal = (new_goal_x, new_goal_y)
                    game_grid[new_goal_x][new_goal_y] = 2


                    path_start = pf.find_path(game_grid, (x_coord, y_coord))


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_down = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_down:
                mouse_x, mouse_y = event.pos
                new_x = mouse_x // cell_length
                new_y = mouse_y // cell_length

                if game_grid[new_x][new_y] == 0:
                    # player moves
                    game_grid[x_coord][y_coord] = 0
                    x_coord = new_x
                    y_coord = new_y
                    game_grid[x_coord][y_coord] = 3

                    path_start = pf.find_path(game_grid, (x_coord, y_coord))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if pf.dirNum == 4:
                    pf = PathFinder(8)
                    neighbour = font.render("neighbours q: 4 (8)", True, BLACK)
                else:
                    pf = PathFinder(4)
                    neighbour = font.render("neighbours q: (4) 8", True, BLACK)
                path_start = pf.find_path(game_grid, (x_coord, y_coord))
 
    dis.fill(WHITE)



    # walls
    for wall in walls:
        pygame.draw.rect(dis, BLACK, [wall[0]*cell_length, wall[1]*cell_length, cell_length, cell_length])

    # player
    pygame.draw.rect(dis, RED, [x_coord*cell_length, y_coord*cell_length, cell_length, cell_length])

    # path
    while (path.parent != None):
        pygame.draw.rect(dis, YELLOW, [path.coord[0]*cell_length, path.coord[1]*cell_length, cell_length, cell_length])
        path = path.parent
    path = path_start

    # goal
    pygame.draw.rect(dis, GREEN, [goal[0]*cell_length, goal[1]*cell_length, cell_length, cell_length])

    # grid
    for i in range (cell_num+1):
        pygame.draw.line(dis, BLACK, (0, cell_length*i), (window_length, cell_length*i))
        pygame.draw.line(dis, BLACK, (cell_length*i, 0), (cell_length*i, window_length))

    # settings
    dis.blit(algo, dest=(window_length+10,0))
    dis.blit(neighbour, dest=(window_length+10,20))
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()