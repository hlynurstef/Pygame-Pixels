""" This module holds the Bitmap class """

from pygame import surfarray as surfarray
from pygame import Surface

from numpy import copyto

class Bitmap():
    """ Bitmap class that holds pixel color information """
    def __init__(self, width, height, surface=None):
        self.width = width
        self.height = height
        if surface:
            self.pixels = surfarray.pixels2d(surface)
        else:
            self.pixels = surfarray.pixels2d(Surface((width, height)))

    def clear(self, color):
        """ Clears the bitmap with a color """
        self.pixels.fill(color.b ^ color.g << 8 ^ color.r << 16)


    def draw(self, bitmap, x_offs, y_offs):
        """
        Draw a new bitmap on top of this bitmap. A color value
        of zero will be ignored and treated as an alpha value.
        """
        x_len = len(bitmap.pixels)
        y_len = len(bitmap.pixels[0])

        # Check if bitmap is outside of screen
        if (x_offs < -x_len or x_offs > self.width or
                y_offs < -y_len or y_offs > self.height):
            return

        x_start = x_offs
        x_end = x_offs + x_len
        y_start = y_offs
        y_end = y_offs + y_len

        x_clip_start = 0
        y_clip_start = 0
        x_clip_end = 0
        y_clip_end = 0

        if x_end > self.width:
            x_clip_end = x_end - self.width
        if y_end > self.height:
            y_clip_end = y_end - self.height

        if x_offs < 0:
            x_clip_start = -x_offs
            x_start = x_offs
        if y_offs < 0:
            y_clip_start = -y_offs
            y_start = y_offs

        # Write bitmap over this bitmap where color is greater than zero.
        # This will allow for the use of bitmasks or "alpha" where color is black
        copyto(self.pixels[
                x_start+x_clip_start:x_end-x_clip_end,
                y_start+y_clip_start:y_end-y_clip_end
            ],
            bitmap.pixels[
                x_clip_start:x_len-x_clip_end,
                y_clip_start:y_len-y_clip_end
            ],
               where=bitmap.pixels[
                x_clip_start:x_len-x_clip_end,
                y_clip_start:y_len-y_clip_end
            ] > 0)
