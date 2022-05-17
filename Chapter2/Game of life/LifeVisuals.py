import pygame
from life import GameGrid
from gameoflife import evolve, draw
import random
from GridManipulation import GridManip


FPS = 15
fpsClock = pygame.time.Clock()

pygame.init()
SCREEN_HEIGHT = 300
SCREEN_WIDTH = 300


win = pygame.display.set_mode((SCREEN_WIDTH+100,SCREEN_HEIGHT+100))

pygame.display.set_caption('Game of Life')

BLACK = (0,0,0)

run = True

Manip = GridManip('confige.txt')
Manip.init()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    
            run = False
    win.fill(BLACK)
    keys = pygame.key.get_pressed()
    
    Manip.gridManip(keys)

    Manip.draw(win)

    pygame.display.update()
    fpsClock.tick(FPS)

   

pygame.quit()
