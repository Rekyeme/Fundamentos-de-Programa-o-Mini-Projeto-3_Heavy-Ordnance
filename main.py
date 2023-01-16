import pygame
import sys
import math
from pygame.locals import *

# General Setup
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)
level = 0
cannon_ = []
for i in range(0, 1):
    cannon_.append(pygame.image.load(f"Assets/Cannon.png"))

# Sprite Import
pygame.image.load(f"Assets/Cannon.png")
pygame.image.load(f"Assets/Cannonball.png")

# Create the display surface and set the caption
window_height = 1000
window_width = 380
SURFACE = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption("Heavy Ordnance")

# Colors
B_Blue = (173, 216, 230)
Grey = (121, 121, 121)
Blue = (9, 129, 209)
Red = (207, 16, 32)


def draw_cannon():
    mouse_pos = pygame.mouse.get_pos()
    cannon_point = (window_width / 2, window_height / 2)
    cannonball = ["Cannonball.png"]
    clicks = pygame.mouse.get_pressed()
    if mouse_pos[0] != cannon_point[0]:
        slope = (mouse_pos[1] - cannon_point[1]) / (mouse_pos[0] - cannon_point[0])
    else:
        slope = -100000
    angle = math.atan(slope)
    rotation = math.degrees(angle)
    if mouse_pos[0] < window_width / 2:
        cannon = pygame.transform.flip(cannon_[level - 1], True, False)
        if mouse_pos[1 < 200]:
            SURFACE.blit(pygame.transform.rotate(cannon, 90 - rotation), (window_width / 2 - 90, window_height - 250))
            if clicks[0]:
                pygame.draw.circle(SURFACE, cannonball[level - 1], mouse_pos, 5)
    else:
        cannon = cannon_[level - 1]
        if mouse_pos[1] < 200:
            SURFACE.blit(
                pygame.transform.rotate((cannon, 270 - rotation), (window_width / 2 - 30, window_height - 250)))
            if clicks[0]:
                pygame.draw.circle(SURFACE, cannonball[level - 1], mouse_pos, 5)


# Main Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            sys.exit()

    # Creates the game background;
    SURFACE.fill(B_Blue)

    # Draws the player area where the cannon is placed (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Grey, [0, 200, 140, 180])

    # Draws the danger zone (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Red, [140, 320, 140, 60])

    # Draws the sea (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Blue, [280, 320, 720, 60])

    # Draws the cannon base in the player area (X, Y, WIDTH, HEIGHT)
    pygame.draw.rect(SURFACE, Blue, [40, 160, 60, 40])

    if level > 0:
        draw_cannon()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
