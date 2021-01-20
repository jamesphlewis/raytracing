from random import random
from utils import Clamp


def PrintVec(v):
    print("{} {} {}".format(v.e[0], v.e[1], v.e[2]))

def PrintColor(v, samples_per_pixel):
    r = v.x()
    g = v.y()
    b = v.z()

    scale = 1.0 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale
    print("{} {} {}".format(
        int(256 * Clamp(r, 0.0, 0.999)),
        int(256 * Clamp(g, 0.0, 0.999)),
        int(256 * Clamp(b, 0.0, 0.999)),
    ))

