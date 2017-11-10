""" Bitmap3D """

import math

from .bitmap import Bitmap
from ..utils.utilities import current_time_millis

class Bitmap3D(Bitmap):
    """ Bitmap 3D class for projections """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.z_buffer = Bitmap(width, height)

    def render(self, game):
        """ Renders the floor """
        # TODO: optimize this function!

        eye = math.sin(game.time/10)*2
        for y in range(0, self.height):

            yd = ((y + 0.5) - self.height / 2) / self.height

            z = (4 + eye) / yd

            if yd < 0:
                z = (4 - eye) / -yd

            for x in range(0, self.width):
                
                xd = ((x) - self.width / 2) / self.height
                xd = xd * z
                xx = int(xd + game.time * 0.1) & 7
                yy = int(z + game.time * 0.1) & 7
                #self.pixels[x,y] = (xx * 16) | (zz * 16) << 8
                self.z_buffer.pixels[x,y] = z
                self.pixels[x,y] = game.art.floors.pixels[xx, yy]

    def post_process(self):
        """ Post processing """
        # TODO: optimize this function!

        for i in range(0, self.width):
            for j in range(0, self.height):
                col = self.pixels[i, j]
                brightness = int(255 - self.z_buffer.pixels[i,j])

                if brightness < 0:
                    brightness = 0

                r = (col >> 16) & 0xff
                g = (col >> 8) & 0xff
                b = (col) & 0xff

                r = int(r * brightness / 255)
                g = int(g * brightness / 255)
                b = int(b * brightness / 255)

                self.pixels[i, j] = r << 16 | g << 8 | b
