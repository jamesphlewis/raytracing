package main

import (
    "fmt"
    "go-ray-tracer/pkg/vec3"
    "go-ray-tracer/pkg/vec3util"
)

const img_width = 256
const img_height = 256

func main() {

    fmt.Println("P3\n", img_width, " ", img_height, "\n255\n")
    for i := img_height - 1; i >= 0; i-- {
        for j := 0; j < img_width; j++ {
            v := vec3.Vec3Builder(float64(j)/(img_width-1), float64(i)/(img_height-1), 0.25)

            fmt.Print(vec3util.WriteColor(&v))
        }
    }

}
