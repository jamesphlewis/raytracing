package vec3

import (
    "testing"
)

func TestMultiply(t *testing.T) {
    lv := Vec3{[3]float64{1, 2, 3}}
    rv := Vec3{[3]float64{1, 2, 3}}

    ov := lv.Multiply(rv)
    if ov.X() != 1 {
        t.Error("Expected X to be 1")
    }
    if ov.Y() != 4 {
        t.Error("Expected Y to be 4")
    }
    if ov.Z() != 9 {
        t.Error("Expected Z to be 9")
    }
}
