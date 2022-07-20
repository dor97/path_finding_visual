import pygame
from queue import Queue

# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 255, 0)
# YELLOW = (255, 255, 0)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# PURPLE = (128, 0, 128)
# ORANGE = (255, 165 ,0)
# GREY = (128, 128, 128)
# TURQUOISE = (64, 224, 208)


def Algorithm_bfs(draw, grid, start, end):
    que = Queue()
    come_from = {}
    que.put(start)
    #map = {spot : 1 for row in grid for spot in row}
    #map[start] = 0
    while not que.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = que.get()

        if current == end:
            reconstruct_path(come_from, end, draw)
            end.make_stat(TURQUOISE)
            return True

        for neighbor in current.neighbors:
            if neighbor.is_open(): #map[neighbor] == 1 and 
                come_from[neighbor] = current
                neighbor.make_stat(GREEN)
                que.put(neighbor)
                #map[neighbor] = 0

        draw()
        if current != start:
            current.make_stat(RED)

    return False


def reconstruct_path(come_from, current, draw):
    while current in come_from:
        current.make_stat(PURPLE)
        current = come_from[current]
        draw()
    current.make_stat(ORANGE)