import sys
import pygame

class Game():
    def __init__(self):
        self.time = 0
    
    def tick(self):
        self.time = self.time + 1
        self.check_events()

    def check_events(self):
        """Check for events and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                print('Average FPS:', sum(self.fps)/len(self.fps))
                pygame.quit()
                sys.exit()