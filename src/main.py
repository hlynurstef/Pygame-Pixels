""" Initializes and runs the program """

import pygame

from . import settings as s
from .graphics.renderer import Renderer

def main():
    pygame.init()
    display = pygame.display.set_mode((s.WIDTH * s.SCALE, s.HEIGHT * s.SCALE))
    pygame.display.set_caption('Pixels | FPS: 0')
    Renderer(display).run()
