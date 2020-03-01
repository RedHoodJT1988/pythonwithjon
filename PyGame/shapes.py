import pygame, sys
from pygame.locals import *

pygame.init()

# set up window
displaysurf = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption("Shapes")

# choose our colors
aqua = (0, 255, 255)
blue = (0, 0, 255)
green = (0, 128, 0)
navy_blue = (0, 0, 128)
black = (0, 0, 0)
lime = (  0, 255,   0)

# draw our surface object
displaysurf.fill(black)
pygame.draw.polygon(displaysurf, aqua, ((150, 0), (291, 150), (235, 270), (56, 270), (0, 150)))
pygame.draw.line(displaysurf, navy_blue, (60, 60), (120, 50), 4)
pygame.draw.circle(displaysurf, green, (300, 50), 20, 0)
pygame.draw.rect(displaysurf, lime, (200, 150, 100, 50))

pixObj = pygame.PixelArray(displaysurf)
pixObj[480][380] = black
pixObj[482][382] = black
pixObj[484][384] = black
pixObj[486][386] = black
pixObj[488][388] = black

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()