import pygame
import sys
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((1000, 380))
pygame.display.set_caption("Heavy Ordnance")
clock = pygame.time.Clock()

# Colors
B_Blue = (173, 216, 230)
Grey = (121, 121, 121)
Blue = (9, 129, 209)
Danger = (207, 16, 32)

# Game Loop Main
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    SURFACE.fill(B_Blue)    # Creates the game background;
    pygame.draw.rect(SURFACE, Grey, (0, 260, 200, 280))     # Draws the base where the cannon is placed;
    pygame.draw.rect(SURFACE, Danger, (200, 360, 140, 360))   # Draws the danger zone;
    pygame.draw.rect(SURFACE, Blue, (340, 360, 1000, 200))  # Draws the sea;

    pygame.display.update()
    clock.tick(60)
