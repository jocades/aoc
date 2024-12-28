fn main() {
    let out = std::io::stdin()
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let (a, b) = line.split_once(",").unwrap();
            (
                a.split_once('-')
                    .map(|(min, max)| (min.parse::<i32>().unwrap(), max.parse::<i32>().unwrap()))
                    .unwrap(),
                b.split_once('-')
                    .map(|(min, max)| (min.parse::<i32>().unwrap(), max.parse::<i32>().unwrap()))
                    .unwrap(),
            )
        })
        .filter(|((amin, amax), (bmin, bmax))| {
            amin >= bmin && amax <= bmax || bmin >= amin && bmax <= amax
        })
        .count();

    // let mut out = 0;
    /* for line in std::io::stdin().lines() {
        let line = line.unwrap();
        let (a, b) = line.split_once(",").unwrap();
        let (amin, amax) = a
            .split_once('-')
            .map(|(min, max)| (min.parse::<i32>().unwrap(), max.parse::<i32>().unwrap()))
            .unwrap();
        let (bmin, bmax) = b
            .split_once('-')
            .map(|(min, max)| (min.parse::<i32>().unwrap(), max.parse::<i32>().unwrap()))
            .unwrap();
        if amin >= bmin && amax <= bmax || bmin >= amin && bmax <= amax {
            out += 1;
        }
    } */

    println!("{out}");
}
