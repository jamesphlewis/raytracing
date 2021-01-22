import math
from random import random
from utils import Clamp

class Vec3():
    def __init__(self, e0, e1, e2):
        self.e = [None, None, None]
        self.e[0] = e0
        self.e[1] = e1
        self.e[2] = e2

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0]**2 + self.e[1]**2 + self.e[2]**2

    def negate(self):
        return self.__class__(-self.e[0], -self.e[1], -self.e[2])

    def increment(self, c):
        self.e[0] += c
        self.e[1] += c
        self.e[2] += c

    def multiply_by_constant(self, constant):
        self.e[0] *= constant
        self.e[1] *= constant
        self.e[1] *= constant

    def divide_by_constant(self, constant):
        return self.multiply_by_constant(1/constant)

    @classmethod
    def random(cls):
        return cls.Vec3(random(), random(), random())

    @classmethod
    def random_clamp(cls, min, max):
        return cls(Clamp(random(), min, max), Clamp(random(), min, max), Clamp(random(), min, max))

    def near_zero(self):
        zero = 0.00000001
        return (abs(self.e[0]) < zero and abs(self.e[1]) < zero and abs(self.e[2]) < zero)

Point3 = Vec3
Color = Vec3


