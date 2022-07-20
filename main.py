import pygame
import random
from spot import Spot
from algorithm import Algorithm_bfs , Algorithm_Astar


WIDTH = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def make_grid(rows, width):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Spot(i, j, width // rows, rows))
    return grid


def draw(win, grid, rows, width):
    win.fill(WHITE)
    gap = width // rows
    for i in grid:
        for spot in i:
            spot.draw(win)

    for i in range(rows):
        pygame.draw.line(win, GREY, (i * gap ,0), (i * gap, width))
        pygame.draw.line(win, GREY, (0 ,i * gap), (width , i * gap))

    pygame.display.update()


def get_rowAndCol(x, y, rows, width):
    gap = width // rows
    return (y // gap, x // gap)


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #quit program
                run = False
            
            if pygame.mouse.get_pressed()[0]:       #drow obstacles
                x , y = pygame.mouse.get_pos()
                row, col = get_rowAndCol(x, y, ROWS, width)
                point = grid[row][col]
                if not start and point != end:
                    point.make_stat(ORANGE)         #start point
                    start = point
                elif not end and point != start:
                    point.make_stat(TURQUOISE)      #end point
                    end = point
                elif point != start and point != end:
                    point.make_stat(BLACK)          #obstacle

            if pygame.mouse.get_pressed()[2]:       #clear obstacles
                x , y = pygame.mouse.get_pos()
                row, col = get_rowAndCol(x, y, ROWS, width)
                point = grid[row][col]
                point.make_stat(WHITE)              #open path
                if point == start:
                    start = None
                if point == end:
                    end = None
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:     #clear screan
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_q:     #creat random maze
                    for row in grid:
                        for point in row:
                            if point != start and end != point:
                                if point.color != WHITE:
                                    point.color = WHITE
                                if random.random() < 0.3:
                                    point.make_stat(BLACK)      #obstacle

                if event.key == pygame.K_SPACE and start and end:       #start path finding
                    for row in grid:
                        for point in row:
                            point.rest()
                            point.update_neighbors(grid)

                    #Algorithm_bfs(lambda : draw(win, grid, ROWS, width), grid, start, end)
                    Algorithm_Astar(lambda : draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_r:     #clear all obstacals
                    for row in grid:
                        for point in row:
                            point.rest()

if __name__ == "__main__":
    main(WIN, WIDTH)