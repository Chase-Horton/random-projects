from settings import *
import pygame as pg
from maze import generateMaze
_ = False
mini_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
mini_map3 = [
    [1, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, 1, 1, 1, _, 1, 1, 1, 1],
    [1, _, 1, _, _, _, _, _, _, _],
    [1, _, _, 1, _, 1, _, _, _, 1],
    [1, _, 1, 1, _, 1, _, 1, 1, 1],
    [1, _, _, _, _, _, _, 1, _, 1],
    [1, _, 1, _, 1, _, 1, 1, _, 1],
    [1, _, 1, 1, _, _, 1, 1, _, 1],
    [1, _, _, 1, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = generateMaze(10, 10)
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, tile in enumerate(row):
                if tile == 1:
                    self.world_map[(i, j)] = True
    def get_start_pos(self):
        start_row = self.mini_map[0]
        for i in range(len(start_row)):
            if start_row[i] == '_':
                return i + 0.5, 0.2
    def draw(self):
        self.get_map()
        [pg.draw.rect(self.game.screen, 'white', (x * TILE, y * TILE, TILE, TILE), 2) for x, y in self.world_map if self.world_map[(x, y)]]