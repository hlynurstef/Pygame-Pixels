""" Game """

import sys
import pygame

class Game():
    """ The main Game class that handles all game logic """
    def __init__(self):
        self.time = 0

    def tick(self):
        """ This function is called on every frame, game logic goes here """
        self.check_events()

    def check_events(self):
        """Check for events and respond to them."""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT
                    or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
