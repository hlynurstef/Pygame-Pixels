""" Utilities module """

import time

def scale(dst, src, s):
    """ Fill array dst with array src scaled by s. """
    Y = dst.shape[0]
    X = dst.shape[1]
    for y in range(0, s):
        for x in range(0, s):
            dst[y:Y:s, x:X:s] = src

def current_time_millis():
    """ Returns the current time in milliseconds. """
    return int(round(time.time() * 1000))
