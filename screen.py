""" Screen module for the virtual screen. """

from random import randrange
import math

from bitmap import Bitmap

from utils import current_time_millis

class Screen(Bitmap):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.testBitmap = Bitmap(64,64)

        for y in range (0, 64):
            for x in range (0, 64):
                r = randrange(0, 256)
                g = randrange(0, 256)
                b = randrange(0, 256)
                self.testBitmap.pixels[x, y] = (b ^ g << 8 ^ r << 16) * int(randrange(0,100)/97)
                

    def render(self, game):
        """ Render images to the virtual screen. """
        # Clear the screen
        self.pixels.fill(0)
        x = int((self.width - 64) / 2)
        y = int((self.height - 64) / 2)
        for i in range(0,100):
            dx = int(math.sin((game.time+i)%2000/2000*math.pi*2)*100)
            dy = int(math.cos((game.time+i)%2000/2000*math.pi*2)*60)
            self.draw(self.testBitmap, x+dx, y+dy)
        

        
        