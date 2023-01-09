import pygame, sys
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((1000, 380))
pygame.display.set_caption("Heavy Ordnance")

B_Blue = (173, 216, 230)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE:
               pygame.quit()
               sys.exit()

    SURFACE.fill(B_Blue)

    pygame.display.update()


