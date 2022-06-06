import pygame
from pygame.locals import *

from ColorImage import ColorImage,RGBColor



def DrawOnImage(MouseObj, Image):
	mouseKey = MouseObj.get_pressed()
	mousePos = MouseObj.get_pos()
	
	if mouseKey[0] == MOUSECLICK:
		pygame.draw.rect(window, (255,255,255),[mousePos[0], mousePos[1], 20,20], 0)
		Image[mousePos[1]//25,mousePos[0]//25] = RGBColor(255,255,255)

	if mouseKey[2] == MOUSECLICK:
		window.fill(BLACK.RGB())
		Image.Image()
		Image.clear(BLACK)
				

def DrawImage(Image,height,width, MousePos = None):
	w_pos =  width//Image.width()
	h_pos = height//Image.height()
	mouseKey = pygame.mouse.get_pressed()
	pygame.draw.rect(window, (255,255,255),[250, 250, w_pos,h_pos], 0)

	if mouseKey[2] == MOUSECLICK:
		window.fill(BLACK.RGB())
		Image.Image()


	for i in range(Image.width()):
		for j in range(Image.height()):
			pygame.draw.rect(window, Image[i,j].RGB(),
                 [i * w_pos, j * h_pos, w_pos, h_pos], 0)
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((400, 400))
 
# Fill the scree with white color
window.fill((0, 0, 0))
 
clock = pygame.time.Clock()
running = True

# Mouse click
MOUSECLICK = 1

# colors
BLACK = RGBColor(0,0,0)
WHITE = RGBColor(255,255,255)


Image = ColorImage(50,50)
Image.clear(BLACK)
# Image.ImageNoise()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	Image.ImageNoise()		
	DrawImage(Image, window.get_width(),window.get_height(), pygame.mouse.get_pos())
	# DrawOnImage(pygame.mouse, Image)
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()

