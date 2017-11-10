""" Handles all rendering to the actual screen """

import pygame
import pygame.surfarray as surfarray

from .. import settings as s
from ..utils.utilities import scale

from ..game.game import Game
from ..graphics.screen import Screen

class Renderer():
    """ Renders to the screen """
    def  __init__(self, display):
        self.time = 0
        self.running = True

        self.pixels = surfarray.pixels2d(display)
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.screen = Screen(s.WIDTH, s.HEIGHT)

    def run(self):
        """ Runs the main render loop """
        last_time = 0

        dt = self.clock.tick(s.FPS)
        self.time = self.time + (dt/1000)
        frames = 0
        while self.running:
            self.tick()
            self.render()
            frames = frames + 1

            dt = self.clock.tick()
            self.time = self.time + dt
            if self.time - last_time > 1000:
                pygame.display.set_caption('Pixels | FPS: ' + str(frames))
                last_time = last_time + 1000
                #print('FPS:',frames)
                frames = 0


    def tick(self):
        """ All game logic goes here. """
        self.game.tick()


    def render(self):
        """ All of the rendering takes place here. """
        self.screen.render(self.game)

        scale(self.pixels, self.screen.pixels, s.SCALE)

        pygame.display.update()
