import pygame
from pygame.locals import *

from ColorImage import ColorImage,RGBColor

def DrawImage(Image,height,width, MousePos):
	print(MousePos)
	w_pos =  width//Image.width()
	h_pos = height//Image.height()
	for i in range(Image.width()):
		for j in range(Image.height()):
			# pygame.draw.rect(window, Image[i,j].RGB(),
   #               [i * w_pos, j * h_pos, w_pos, h_pos], 0)
			pygame.draw.rect(window, (255,255,255),
                 [MousePos[0], MousePos[1], w_pos, h_pos], 0)
				


			# if ((i * w_pos,j * h_pos) == MousePos):
			# 	pygame.draw.rect(window, (255,255,255),
   #               [MousePos[0], MousePos[1], w_pos, h_pos], 0)
			# 	Image[i,j] == RGBColor(255,255,255)


 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((500, 500))
 
# Fill the scree with white color
window.fill((0, 0, 0))
 
clock = pygame.time.Clock()
running = True

BLACK = RGBColor(0,0,0)
Image = ColorImage(20,20)
Image.clear(BLACK)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Fill the scree with white color
	 
	# Using draw.rect module of
	# pygame to draw the solid circle
	# Image.ImageNoise()
	mouse = pygame.mouse.get_pos()
	DrawImage(Image, window.get_width(),window.get_height(),mouse)
	# window.fill((0, 0, 0))

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()

