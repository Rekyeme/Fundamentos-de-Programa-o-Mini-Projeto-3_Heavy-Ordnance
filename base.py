import pygame
from main import SURFACE, Grey


class Base:
    def __init__(self):
        pygame.draw.rect(SURFACE, Grey, (0, 260, 200, 280))
