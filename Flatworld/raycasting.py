import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game
    
    def ray_cast(self):
        outDepths = []
        outAngles = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
             
            delta_depth = dy/sin_a
            dx = delta_depth * cos_a

            for i in range(0, RENDER_DISTANCE):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth
            
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
             
            delta_depth = dx/cos_a
            dy = delta_depth * sin_a

            for i in range(0, RENDER_DISTANCE):
                tile_hor = int(x_vert), int(y_vert)
                if tile_hor in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            #depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor
            #draw line from ox, oy * tile to depth
            outDepths.append(depth)
            outAngles.append(ray_angle)
            ray_angle += DELTA_ANG
        normFactor = RENDER_DISTANCE
        normDepths = []
        for depth in outDepths:
            if depth < normFactor:
                normDepths.append(depth/normFactor)
            else:
                normDepths.append(1)
        depths_and_angs = zip(normDepths, outAngles)
        for depth, ray_angle in depths_and_angs:
            x = normFactor* depth * math.cos(ray_angle) * TILE
            y = normFactor* depth * math.sin(ray_angle) * TILE
            color = (255 * (1-depth), 0, 150)
            if self.game.MODE == "2D":
                pg.draw.line(self.game.screen, color, (ox*TILE, oy*TILE), (ox*TILE + x, oy*TILE + y), 2)
        return normDepths
    def update(self):
        return self.ray_cast()