import pygame

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


class Spot: 
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = col * width
        self.y = row * width
        self.color = WHITE
        self.total_rows = total_rows
        self.neighbors = []

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def make_stat(self, color):
        self.color = color

    def rest(self):
        if self.color == RED or self.color == GREEN or self.color == PURPLE:
            self.color = WHITE

    def getPos(self):
        return self.row, self.col

    def get_stat(self):
        return self.color

    def is_barrier(self):
        return self.color == BLACK

    def is_open(self):
        return (self.color == WHITE or self.color == TURQUOISE)

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.col < self.total_rows - 1  and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
        if self.row < self.total_rows - 1  and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0  and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.row > 0  and self.col > 0 and not grid[self.row - 1][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col - 1])

        if self.row > 0  and self.col < self.total_rows - 1 and not grid[self.row - 1][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col + 1]) 

        if self.row < self.total_rows - 1  and self.col > 0 and not grid[self.row + 1][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col - 1]) 

        if self.row < self.total_rows - 1  and self.col < self.total_rows - 1 and not grid[self.row + 1][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col + 1])  
    # def is_start(self):
    #     return self.color == 
