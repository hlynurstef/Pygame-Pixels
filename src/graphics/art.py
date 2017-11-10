""" Art """
import os
import pygame

from .bitmap import Bitmap

class Art():
    """ A class for art """
    def __init__(self):
        print(os.getcwd())
        self.floors = self.load_bitmap(os.path.join('assets', 'tex', 'floors.png'))


    def load_bitmap(self, img_path):
        """ Loads an image and returns it as a Bitmap """
        img = pygame.image.load(img_path).convert()
        return Bitmap(img.get_width(), img.get_height(), img)
