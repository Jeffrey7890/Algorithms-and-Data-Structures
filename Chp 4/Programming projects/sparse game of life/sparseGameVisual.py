import sys

import pygame
from SparseGameGrid import Grid
from gameofLife import evolve	 
import random

from configuration import configuration

commanLine = sys.argv
configure = configuration("slider gun")
(row, col), configure = configure[1], configure[0]


if len(commanLine) == 2:
	if type(commanLine[1]) == str:
		configure = configuration(commanLine[1])
		(row, col), configure = configure[1],configure[0]
	elif type(commanLine[1]) == list:
		configure = commanLine[1]


FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()

SCREEN_HEIGHT = 120
SCREEN_WIDTH = 500


win = pygame.display.set_mode((SCREEN_WIDTH+100,SCREEN_HEIGHT+100))

pygame.display.set_caption('Sparse Game of Life')

BLACK = (0,0,0)
WHITE = (255,255,255)


def drawSparseGame(grid, width, height):
	grid.configure(evolve(grid))
	for i in range(len(grid)):
		cell = grid._elementList[i]
		pygame.draw.rect(win, WHITE, (width * cell.row + cell.row, height * cell.col + cell.col, width, height ))
		

grid = Grid(row,col, configure)
run = True

while run: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.fill(BLACK)

	
	drawSparseGame(grid,5, 5 )

	pygame.display.update()
	fpsClock.tick(FPS)

   

pygame.quit()