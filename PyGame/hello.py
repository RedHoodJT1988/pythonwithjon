import sys, pygame
from pygame.locals import *

pygame.init()

displaysurf = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Hi")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()