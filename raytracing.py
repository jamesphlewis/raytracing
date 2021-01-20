import math
from random import random
from camera import Camera
from vec3 import Vec3, Color, Point3
from sphere import Sphere
from ray import Ray, RayColor
from vec3_utils import DivideVectorByConstant, MultiplyVectorByConstant, AddVectors, SubtractVectors
from print_utils import PrintColor

SAMPLES_PER_PIXEL = 100
ASPECT_RATIO = 16.0 / 9.0
IMG_WIDTH = 400
IMG_HEIGHT = int(IMG_WIDTH / ASPECT_RATIO)

def makeImage():
    world = [Sphere(Point3(0, 0, -1), 0.5),
        Sphere(Point3(0, -100.5, -1), 100),]

    cam = Camera()
    print("P3\n{} {} \n255".format(IMG_WIDTH, IMG_HEIGHT))
    for j in range(IMG_HEIGHT, 0, -1):
        for i in range(IMG_WIDTH):
            c = Color(0, 0, 0)
            for k in range(SAMPLES_PER_PIXEL):
                u = float(i + random()) / (IMG_WIDTH - 1)
                v = float(j + random()) / (IMG_HEIGHT - 1)
                r = cam.get_ray(u, v)
                c = AddVectors(c, RayColor(r, world))
            PrintColor(c, SAMPLES_PER_PIXEL)


if __name__ == "__main__":
    makeImage();