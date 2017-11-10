import sys

import pygame
import numpy as N
import pygame.surfarray as surfarray

import settings as s
from game import Game
from screen import Screen
from utils import scale

class Renderer():
    def  __init__(self, display):
        self.WIDTH = 160
        self.HEIGHT = 120
        self.SCALE = 4
        self.FPS = 60
        self.time = 0
        self.running = True

        self.pixels = surfarray.pixels2d(display)
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.screen = Screen(s.WIDTH, s.HEIGHT)

    def run(self):
        lastTime = 0

        dt = self.clock.tick(self.FPS)
        self.time = self.time + (dt/1000)
        frames = 0
        while self.running:
            self.tick()
            self.render()
            frames = frames + 1

            dt = self.clock.tick()
            self.time = self.time + dt
            if self.time - lastTime > 1000:
                pygame.display.set_caption('Pixels | FPS: ' + str(frames))
                lastTime = lastTime + 1000
                print('FPS:',frames)
                frames = 0


    def tick(self):
        """ All game logic goes here. """
        self.game.tick()


    def render(self):
        """ All of the rendering takes place here. """
        self.screen.render(self.game)

        scale(self.pixels, self.screen.pixels, s.SCALE)

        pygame.display.update()

    

def main():
    pygame.init()
    display = pygame.display.set_mode((s.WIDTH*s.SCALE, s.HEIGHT*s.SCALE))

    Renderer(display).run()


if __name__ == '__main__':
    main()
