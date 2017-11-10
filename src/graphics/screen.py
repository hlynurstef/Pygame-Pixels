""" Screen module for the virtual screen. """

from random import randrange
import math

from .. import settings as s
from .bitmap import Bitmap
from .color import Color

from ..utils.utilities import current_time_millis

class Screen(Bitmap):
    """
    Virtual screen where all images are drawn before being
    projected onto the actual screen.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.clear_color = Color(0, 0, 0)
        self.test_bitmap = Bitmap(64, 64)
        self.panel = Bitmap(width, s.PANEL_HEIGHT)
        self.viewport = Bitmap(width, height-s.PANEL_HEIGHT)

        for y in range(0, 64):
            for x in range(0, 64):
                r = randrange(0, 256)
                g = randrange(0, 256)
                b = randrange(0, 256)
                self.test_bitmap.pixels[x, y] = (b ^ g << 8 ^ r << 16) * randrange(0, 2)


    def render(self, game):
        """ Render images to the virtual screen. """
        # Clear the screen
        self.clear_screen(self.clear_color)

        x = int((self.panel.width - 64) / 2)
        y = int((self.panel.height - 64) / 2)
        #for i in range(0,100):
        dx = int(math.sin((current_time_millis())%2000/2000*math.pi*2)*100)
        #dy = int(math.cos((current_time_millis())%2000/2000*math.pi*2)*60)
        self.panel.draw(self.test_bitmap, x+dx, y)
        self.draw(self.panel, 0, self.height-s.PANEL_HEIGHT)
        self.draw(self.viewport, 0, 0)


    def clear_screen(self, color):
        """ Clears the entire screen. """
        self.clear(color)
        self.panel.clear(color)
        self.viewport.clear(color)
