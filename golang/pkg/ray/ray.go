package ray

import (
    "go-ray-tracer/pkg/vec3"
)

type Ray struct {
    origin    vec3.Vec3
    direction vec3.Vec3
}

func RayBuilder(o vec3.Vec3, d vec3.Vec3) (r Ray) {
    r = Ray{o, d}
    return
}

func (r Ray) Origin() (v *vec3.Vec3) {
    v = &r.origin
    return
}

func (r Ray) Direction() (v *vec3.Vec3) {
    v = &r.direction
    return
}

func (r Ray) At(t float64) (v vec3.Vec3) {
    v = r.Origin().Add(r.Direction().MultiplyScalar(t))
    return
}
