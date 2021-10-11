fn main() {
    let image_width = 256;
    let image_height = 256;
    let mut r: f64;
    let mut g: f64;
    let mut b: f64;
    let mut ir: i32;
    let mut ig: i32;
    let mut ib: i32;
    println!("P3\n{} {}\n255\n", image_width, image_height);
    for j in (0..image_height).rev() {
        for i in 0..image_width {
            r = (i as f64) / ((image_width - 1) as f64);
            g = (j as f64) / ((image_height - 1) as f64);
            b = 0.25;
            // println!("Hello, world!");
            ir = (r * 255.999) as i32;
            ig = (g * 255.999) as i32;
            ib = (b * 255.999) as i32;
            print!("{} {} {}\n", ir, ig, ib);
        }
    }
}
