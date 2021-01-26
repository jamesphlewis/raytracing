package vec3

import (
    "math"
)

type Vec3 struct {
    e [3]float64
}

func Vec3Builder(x float64, y float64, z float64) (v Vec3) {
    v = Vec3{[3]float64{x, y, z}}
    return
}

func (lv Vec3) X() (x float64) {
    return lv.e[0]
}

func (lv Vec3) Y() (y float64) {
    return lv.e[1]
}

func (lv Vec3) Z() (z float64) {
    return lv.e[2]
}

func (lv Vec3) Negate() {
    lv.e[0] = -lv.e[0]
    lv.e[1] = -lv.e[1]
    lv.e[2] = -lv.e[2]
    return
}

func (lv Vec3) Increment(rv *Vec3) {
    lv.e[0] += rv.e[0]
    lv.e[1] += rv.e[1]
    lv.e[2] += rv.e[2]
    return
}

func (lv Vec3) Decrement(rv *Vec3) {
    lv.e[0] -= rv.e[0]
    lv.e[1] -= rv.e[1]
    lv.e[2] -= rv.e[2]
    return
}

func (lv Vec3) ScaleUp(sf float64) {
    lv.e[0] *= sf
    lv.e[1] *= sf
    lv.e[2] *= sf
    return
}

func (lv Vec3) ScaleDown(sf float64) {
    lv.ScaleUp(1 / sf)
    return
}

func (lv Vec3) Add(rv Vec3) (ov Vec3) {
    ov = Vec3Builder(lv.e[0]+rv.e[0], lv.e[1]+rv.e[1], lv.e[2]+rv.e[2])
    return
}

func (lv Vec3) Subtract(rv Vec3) (ov Vec3) {
    ov = Vec3Builder(lv.e[0]-rv.e[0], lv.e[1]-rv.e[1], lv.e[2]-rv.e[2])
    return
}

func (lv Vec3) Multiply(rv Vec3) (ov Vec3) {
    ov = Vec3Builder(lv.e[0]*rv.e[0], lv.e[1]*rv.e[1], lv.e[2]*rv.e[2])
    return
}

func (lv Vec3) MultiplyScalar(sf float64) (ov Vec3) {
    ov = Vec3Builder(lv.e[0]*sf, lv.e[1]*sf, lv.e[2]*sf)
    return
}

func (lv Vec3) Divide(sf float64) (ov Vec3) {
    ov = lv.MultiplyScalar(1 / sf)
    return
}

func (lv Vec3) Dot(rv Vec3) (oi float64) {
    oi = lv.e[0]*rv.e[0] + lv.e[1]*rv.e[1] + lv.e[2]*rv.e[2]
    return
}

func (lv Vec3) Cross(rv Vec3) (ov Vec3) {
    ov = Vec3Builder(
        lv.e[1]*rv.e[2]-lv.e[2]*rv.e[1],
        lv.e[2]*rv.e[0]-lv.e[0]*rv.e[2],
        lv.e[0]*rv.e[1]-lv.e[1]*rv.e[0],
    )
    return
}

func (lv Vec3) LengthSquared() (l float64) {
    l = lv.e[0]*lv.e[0] + lv.e[1]*lv.e[1] + lv.e[2]*lv.e[2]
    return
}

func (lv Vec3) Length() (l float64) {
    l = math.Sqrt(lv.LengthSquared())
    return
}
