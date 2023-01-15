import pygame
import sys
from pygame.locals import *

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
window_height = 1000
window_width = 380
SURFACE = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption("Heavy Ordnance")

# Colors
B_Blue = (173, 216, 230)
Grey = (121, 121, 121)
Blue = (9, 129, 209)
Danger = (207, 16, 32)


# Sprites


# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Creates the game background;
    SURFACE.fill(B_Blue)

    # Draws the player area where the cannon is placed;(X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Grey, [0, 200, 140, 180])

    # Draws the danger zone; (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Danger, [140, 320, 140, 60])

    # Draws the sea; (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Blue, [280, 320, 720, 60])

    # Draws the cannon base in the player area; (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Blue, [40, 160, 60, 40])

    pygame.display.flip()
    clock.tick(60)
