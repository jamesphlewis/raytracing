import math
from hittable import HitRecord
from vec3 import Color, Point3, Vec3
from vec3_utils import SubtractVectors, Dot, DivideVectorByConstant, UnitVector

class Sphere():
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, ray, t_min, t_max):
        oc = SubtractVectors(ray.origin, self.center)
        a = ray.direction.length_squared()
        half_b = Dot(oc, ray.direction)
        c = oc.length_squared() - self.radius**2
        discriminant = half_b**2 - a*c
        if discriminant < 0:
            return False, None
        
        sqrtd = math.sqrt(discriminant)
        root = (-half_b - sqrtd) / a
        if (root < t_min) or (root > t_max):
            root = (-half_b - sqrtd) / a
            if (root < t_min) or (root > t_max):
                return False, None

        p = ray.at(root)
        outward_normal = DivideVectorByConstant(
            SubtractVectors(p, self.center),
            self.radius)

        rec = HitRecord(p, t=root, material=self.material)
        rec.set_front_normal(ray, outward_normal)
        return True, rec


def RandomInUnitSphere():
    while True:
        v = Vec3.random_clamp(-1, 1)
        if v.length_squared() < 1:
            return v

def RandomUnitVector():
    return UnitVector(RandomInUnitSphere())

def RandomInHemisphere(normal):
    us = RandomInUnitSphere()
    if Dot(us, normal) > 0.0:
        return us
    else:
        us.negate()
        return us