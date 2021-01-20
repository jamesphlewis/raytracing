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
