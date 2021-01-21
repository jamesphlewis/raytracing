from math import sqrt
from random import random
from vec3 import Color
from ray import Ray
from vec3_utils import Dot, Reflect, UnitVector, AddVectors, MultiplyVectorByConstant, Refract, Negate
from sphere import RandomUnitVector, RandomInUnitSphere

class Metal():
    def __init__(self, color, fuzz):
        self.albedo = color
        self.fuzz = fuzz if fuzz < 1 else 1

    def scatter(self, r_in, rec):
        ref = Reflect(UnitVector(r_in.direction), rec.normal)
        fuzz_vec = MultiplyVectorByConstant(RandomInUnitSphere(), self.fuzz)
        ref = AddVectors(ref, fuzz_vec)
        scattered = Ray(rec.point, ref)
        attenuation = self.albedo
        return Dot(scattered.direction, rec.normal) > 0, attenuation, scattered

class Lambertian():
    def __init__(self, color):
        self.albedo = color

    def scatter(self, r_in, rec):
        scatter_direction = AddVectors(RandomUnitVector(), rec.normal)
        if scatter_direction.near_zero():
            scatter_direction = rec.normal
        scattered = Ray(rec.point, scatter_direction)
        attenuation = self.albedo
        return True, attenuation, scattered

class Dialectric():
    def __init__(self, index_of_refraction):
        self.index_of_refraction = index_of_refraction

    def scatter(self, r_in, rec):
        attenuation = Color(1.0, 1.0, 1.0)
        refraction_ratio = 1.0 / self.index_of_refraction if rec.front_face else self.index_of_refraction
        unit_dir = UnitVector(r_in.direction)
        cos_theta = min(Dot(Negate(unit_dir), rec.normal), 1.0)
        sin_theta = sqrt(1.0 - cos_theta**2)

        cannot_refract = (refraction_ratio * sin_theta) > 1.0
        direction = None
        if cannot_refract or (Reflectance(cos_theta, refraction_ratio) > random()):
            direction = Reflect(unit_dir, rec.normal)
        else:
            direction = Refract(unit_dir, rec.normal, refraction_ratio)

        scattered = Ray(rec.point, direction)
        return True, attenuation, scattered

def Reflectance(cosine, ref_idx):
    r0 = (1 - ref_idx) / (1 + ref_idx)
    r0 = r0**2
    return r0 + (1 - r0) * pow((1 - cosine), 5)
