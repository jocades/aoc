use regex::Regex;

const INPUT: &'static str = include_str!("input");

fn part1() -> i32 {
    // 161
    let _test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";

    Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)")
        .unwrap()
        .captures_iter(INPUT)
        .map(|c| c.extract())
        .fold(0, |acc, (_, [l, r])| {
            acc + l.parse::<i32>().unwrap() * r.parse::<i32>().unwrap()
        })
}

fn part2() -> i32 {
    // 48
    let _test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

    let mut out = 0;
    let mut enabled = true;
    Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\)|do\(\))")
        .unwrap()
        .captures_iter(INPUT)
        .for_each(|c| {
            if let Some(op) = c.get(3) {
                enabled = op.as_str() == "do()";
            }

            if enabled {
                match (c.get(1), c.get(2)) {
                    (Some(l), Some(r)) => {
                        out +=
                            l.as_str().parse::<i32>().unwrap() * r.as_str().parse::<i32>().unwrap()
                    }
                    _ => (),
                }
            }
        });
    out
}

fn main() {
    println!("part1 = {}", part1());
    println!("part2 = {}", part2());
}
