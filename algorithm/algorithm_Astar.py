import pygame
from queue import PriorityQueue

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

def Algorithm_Astar(draw, grid, start, end):
    open_set = PriorityQueue()
    count = 0
    open_set.put((0, count, start))
    #open_set_hash = {start}
    come_from = {}
    g_score = {spot : float('inf') for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot : float('inf') for row in grid for spot in row}
    f_score[start] = h(start.getPos(), end.getPos()) 

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        #open_set_hash.remove(current)

        if current == end:
            reconstruct_path(come_from, end, draw)
            end.make_stat(TURQUOISE)
            return True

        for neighbor in current.neighbors:
            neighbor_g_score = g_score[current] + 1

            if neighbor_g_score < g_score[neighbor] and neighbor.is_open():
                come_from[neighbor] = current
                g_score[neighbor] = neighbor_g_score
                f_score[neighbor] = neighbor_g_score + h(neighbor.getPos(), end.getPos())
                count += 1
                open_set.put((f_score[neighbor], count, neighbor))
                #open_set_hash.add(neighbor)
                neighbor.make_stat(GREEN)

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

def h(p1, p2):
    x1 , y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)    