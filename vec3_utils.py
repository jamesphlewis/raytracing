from math import sqrt
from vec3 import Vec3

def AddVectors(l, r):
    return Vec3(l.e[0] + r.e[0], l.e[1] + r.e[1], l.e[2] + r.e[2])

def SubtractVectors(l, r):
    return Vec3(l.e[0] - r.e[0], l.e[1] - r.e[1], l.e[2] - r.e[2])

def MultiplyVectors(l, r):
    return Vec3(l.e[0] * r.e[0], l.e[1] * r.e[1], l.e[2] * r.e[2])

def MultiplyVectorByConstant(l, c):
    return Vec3(l.e[0] * c, l.e[1] * c, l.e[2] * c)

def DivideVectorByConstant(l, c):
    return Vec3(l.e[0] / c, l.e[1] / c, l.e[2] / c)

def Dot(l, r):
    return l.e[0] * r.e[0] + l.e[1] * r.e[1] + l.e[2] * r.e[2]

def Cross(l, r):
    return Vec3(l.e[1] * r.e[2] - l.e[2] *r.e[1],
        l.e[2] * r.e[0] - l.e[0] * r.e[2],
        l.e[0] * r.e[1] - l.e[1] * r.e[0])

def UnitVector(v):
    return DivideVectorByConstant(v, v.length())

def Reflect(v, n):
    d = Dot(v, n)
    d = MultiplyVectorByConstant(MultiplyVectorByConstant(n, d), 2)
    return SubtractVectors(v, d)

def Refract(uv, n, etai_over_etat):
    cos_theta = min(Dot(uv.negate(), n), 1)
    r_out_perp = MultiplyVectorByConstant(
        AddVectors(
            MultiplyVectorByConstant(
                n,
                cos_theta
            ),
            uv
        ),
        etai_over_etat
    )
    r_out_parallel = MultiplyVectorByConstant(
        n,
        -sqrt(abs(1.0 - r_out_perp.length_squared()))
    )
    return AddVectors(r_out_parallel, r_out_perp)