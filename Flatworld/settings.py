import math

WIDTH, HEIGHT = 1920,960
FPS = 60

PLAYER_ANGLE = math.pi/2
PLAYER_SPEED = 0.002 
PLAYER_ROTATION_SPEED = 0.001

RENDER_DISTANCE = 10
TILE = 96

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANG = FOV / NUM_RAYS