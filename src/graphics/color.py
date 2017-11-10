""" Color module. """

class Color():
    """ Class representing a color. """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def set(self, r, g, b):
        """ Set color. """
        self.r = r
        self.g = g
        self.b = b
