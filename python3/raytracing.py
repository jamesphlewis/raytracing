import math
from random import random
from material import Metal, Lambertian, Dialectric
from camera import Camera
from vec3 import Vec3, Color, Point3
from sphere import Sphere
from ray import Ray, RayColor
from vec3_utils import DivideVectorByConstant, MultiplyVectorByConstant, AddVectors, SubtractVectors
from print_utils import PrintColor

SAMPLES_PER_PIXEL = 2
ASPECT_RATIO = 16.0 / 9.0
IMG_WIDTH = 400
IMG_HEIGHT = int(IMG_WIDTH / ASPECT_RATIO)

def make_world():
    world = []
    ground = Lambertian(Color(0.5, 0.5, 0.5))
    world.append(Sphere(Point3(0, -1000, 0), 1000, ground))
    num_balls = 2
    for x in range(-num_balls, num_balls):
        for y in range(-num_balls, num_balls):
            mat = random()
            center = Point3(x + 0.9 * random(), 0.2, y + 0.9 * random())

            if (SubtractVectors(center, Point3(4, 0.2, 0)).length() > 0.9):
                if mat < 0.8:
                    color = Color(random(), random(), random())
                    sphere_mat = Lambertian(color)
                    world.append(Sphere(center, 0.2, sphere_mat))
                elif mat < 0.95:
                    color = Color(random(), random(), random())
                    fuzz = random() * 0.5
                    sphere_mat = Metal(color, fuzz)
                    world.append(Sphere(center, 0.2, sphere_mat))
                else:
                    sphere_mat = Dialectric(1.5)
                    world.append(Sphere(center, 0.2, sphere_mat))
    mat1 = Dialectric(1.5)
    world.append(Sphere(Point3(0, 1, 0), 1.0, mat1))
    mat2 = Lambertian(Color(0.4, 0.2, 0.1))
    world.append(Sphere(Point3(-4, 1, 0), 1.0, mat2))
    mat3 = Metal(Color(0.7, 0.6, 0.5), 0.0)
    world.append(Sphere(Point3(4, 1, 0), 1.0, mat3))
    return world


def makeImage():
    world = make_world()

    lookfrom = Point3(13, 2, 3)
    lookat = Point3(0, 0, 0)
    vup = Vec3(0, 1, 0)
    dist_to_focus = 10.0
    aperture = 0.1

    cam = Camera(
        lookfrom,
        lookat,
        vup,
        20,
        ASPECT_RATIO,
        aperture,
        dist_to_focus)
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