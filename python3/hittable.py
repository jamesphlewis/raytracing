import math
from vec3_utils import SubtractVectors, Dot


class HitRecord():
    def __init__(self, point, normal=None, t=0, front_face=True, material=None):
        self.point = point
        self.normal = normal
        self.t = t
        self.front_face = front_face
        self.material = material

    def set_front_normal(self, ray, outward_normal):
        self.front_face = Dot(ray.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else outward_normal.negate()



def HitFromList(ray, t_min, t_max, hittable_list):
    hit_anything = False
    closest_so_far = t_max
    rec = None
    for hittable in hittable_list:
        hit, temp_rec = hittable.hit(ray, t_min, closest_so_far)
        if hit:
            hit_anything = True
            rec = temp_rec
            closest_so_far = rec.t
    return hit_anything, rec

