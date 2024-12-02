const INPUT: &'static str = include_str!("input");

#[allow(dead_code)]
const TEST: &'static str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

fn is_safe(line: &str) -> bool {
    let mut prev: Option<i32> = None;
    let mut dir = 0; // inc = 1 | dec = -1 | first = 0
    for n in line.split_whitespace().map(|w| w.parse::<i32>().unwrap()) {
        if let Some(prev) = prev {
            if (n > prev && dir < 0) || (n < prev && dir > 0) {
                return false;
            }
            let dif = (n - prev).abs();
            if dif > 3 || dif < 1 {
                return false;
            }
            dir = if n < prev { -1 } else { 1 };
        }
        prev = Some(n);
    }
    true
}

fn main() {
    let output = INPUT.lines().filter(|line| is_safe(line)).count();
    println!("{:?}", INPUT.lines().last());
    println!("{output}");
}
