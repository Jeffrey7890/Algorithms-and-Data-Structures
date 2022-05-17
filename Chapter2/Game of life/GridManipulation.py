import pygame
import random

from life import GameGrid
from gameoflife import evolve, draw

WHITE = (255,255,255)
BLACK = (0,0,0)

class GridManip:
	GRID_WIDTH=30
	GRID_HEIGHT = 30

	grid = GameGrid(GRID_WIDTH, GRID_HEIGHT)

	def __init__(self,file_name):
		self.file_name = file_name
		self.INIT_CONFIG = []

	def init(self):
		INIT_CONFIG = [(random.randint(0,self.GRID_WIDTH-1), random.randint(0,self.GRID_HEIGHT-1)) for _ in range(400)]
		self.grid.configure(INIT_CONFIG)


	def gridManip(self, keys):
		if keys[pygame.K_RETURN]:
			self.INIT_CONFIG = [(random.randint(0,self.GRID_WIDTH-1), random.randint(0,self.GRID_HEIGHT-1)) for _ in range(400)]
			self.grid.configure(self.INIT_CONFIG)

		if keys[pygame.K_s]:
			print("Saved !!!!!!!!")
			self.saveConfig()

		if keys[pygame.K_r]:
			self.grid.configure(self.readConfig())
			print("Reading !!!")

	def draw(self,win, width = 10,height = 10):
		self.grid.configure(evolve(self.grid))
		for i in range(self.grid.numRows()):
			for j in range(self.grid.numCols()):
				if self.grid[i,j] == 1:
					pygame.draw.rect(win, self.WHITE,(width *i + i *1, height * j + j *1, width, height))

	def saveConfig(self):
		with open(self.file_name,'wb') as file:
			for i in self.INIT_CONFIG:
				some_bytes = bytearray(list(i))
				file.write(bytes(some_bytes))
		file.close()

	def readConfig(self):
		configs = []
		with open(self.file_name,'rb') as file:
			if file:
				config = list(file.read())
				for i in range(1,len(config)-1,2):
					configs.append((config[i-1], config[i]))
					
		file.close()
		return configs

	def mainLoop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return False
			self.win.fill(BLACK)
			keys = pygame.key.get_pressed()

			self.gridManip(keys)
			gridManip.draw()

			pygame.display.update()
			fpsClock.tick(FPS)
		pygame.quit()

