package vec3util

import (
    "fmt"
    "go-ray-tracer/pkg/vec3"
)

func WriteColor(v *vec3.Vec3) (r string) {
    r = fmt.Sprint(int(255.99*v.X())) + " " + fmt.Sprint(int(255.99*v.Y())) + " " + fmt.Sprint(int(255.99*v.Z())) + "\n"
    return
}
