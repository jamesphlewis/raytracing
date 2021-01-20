from vec3 import Color
from ray import Ray
from vec3_utils import Dot, Reflect, UnitVector, AddVectors, MultiplyVectorByConstant, Refract
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
        refracted = Refract(unit_dir, rec.normal, refraction_ratio)
        scattered = Ray(rec.point, refracted)
        return True, attenuation, scattered