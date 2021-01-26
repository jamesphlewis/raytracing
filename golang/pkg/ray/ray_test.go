package ray

import (
    "go-ray-tracer/pkg/vec3"
    "testing"
)

func TestMultiply(t *testing.T) {
    lv := vec3.Vec3Builder(0.1, 0.2, 0.3)
    rv := vec3.Vec3Builder(0.4, 0.5, 0.4)
    r := RayBuilder(lv, rv)
    ov := r.At(1.0)
    if ov.X() != 0.5 {
        t.Error("Expected X to be 0.5", ov.X())
    }
    if ov.Y() != 0.7 {
        t.Error("Expected Y to be 0.7", ov.Y())
    }
    if ov.Z() != 0.7 {
        t.Error("Expected Z to be 0.7:", ov.Z())
    }
}
