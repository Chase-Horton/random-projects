import pygame as pg
import sys
from settings import *
from map import Map
from player import Player
from raycasting import RayCasting


class Game:
    def __init__(self):
        pg.init()
        self.MODE = '2D'
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.dt = 1
        self.new_game() 

    def new_game(self):
        self.MODE = '2D'
        self.map = Map(self)
        self.player_start_pos = self.map.get_start_pos()
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.won = False

    def update(self):
        self.player.update()
        self.two_d_rays = self.raycasting.update()
        self.drawTwoDRays()
        if(self.player.x > WIDTH / TILE):
            self.won = True
        elif(self.player.y > HEIGHT / TILE):
            self.won = True
        if self.won:
            label = "YOU WIN!"
            font = pg.font.SysFont('consolas', 50, bold=True)
            self.screen.blit(font.render(label, 1, pg.Color('Green')), (900, 500))
        pg.display.flip()
        self.dt = self.clock.tick(FPS)
        pg.display.set_caption("FPS: {:.2f}".format(self.clock.get_fps()))

    def drawTwoDRays(self):
        x = WIDTH // 2
        for ray in self.two_d_rays:
            color = (230*(1-ray), 230*(1-ray), 230*(1-ray))
            pg.draw.line(self.screen, color, (x, 0), (x, HEIGHT), 1)
            x += 1
        label = 'Angle: {:.1f}'.format(self.player.angle * 180 / math.pi)
        #put label on screen
        self.font = pg.font.SysFont('consolas', 20)
        self.screen.blit(self.font.render(label, 1, pg.Color('black')), (970, 10))

    def draw(self):
        self.screen.fill('black')
        if self.MODE == '2D':
            self.map.draw()
            self.player.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_2:
                    self.MODE = '2D'
                elif event.key == pg.K_1:
                    self.MODE = '1D'
                elif event.key == pg.K_r:
                    self.new_game()
    
    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()