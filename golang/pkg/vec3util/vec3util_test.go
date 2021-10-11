package vec3util

import (
    "go-ray-tracer/pkg/vec3"
    "testing"
)

func TestMultiply(t *testing.T) {
    lv := vec3.Vec3Builder(0.1, 0.2, 0.3)
    rep := WriteColor(&lv)
    if rep != "25 51 76\n" {
        t.Error("Expected X to be asdf, was: ", rep)
    }
}
