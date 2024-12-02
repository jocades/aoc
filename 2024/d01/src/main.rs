const INPUT: &'static str = include_str!("input");

#[allow(dead_code)]
const TEST: &'static str = "3   4
4   3
2   5
1   3
3   9
3   3";

fn parse(input: &str, l1: &mut Vec<i32>, l2: &mut Vec<i32>) {
    for line in input.lines() {
        let mut iter = line.split_whitespace();
        l1.push(iter.next().unwrap().parse().unwrap());
        l2.push(iter.next().unwrap().parse().unwrap());
    }
}

fn part1(input: &str) -> i32 {
    let (mut l1, mut l2) = (Vec::new(), Vec::new());
    parse(input, &mut l1, &mut l2);

    l1.sort();
    l2.sort();

    l1.iter().zip(&l2).map(|(&a, &b)| (a - b).abs()).sum()
}

fn part2(input: &str) -> i32 {
    let (mut l1, mut l2) = (Vec::new(), Vec::new());
    parse(input, &mut l1, &mut l2);

    // O(len(l1) * len(l2))
    l1.iter()
        .map(|x| {
            let n = l2.iter().filter(|&y| x == y).count();
            x * n as i32
        })
        .sum()
}

fn part2_with_cache(input: &str) -> i32 {
    let (mut l1, mut l2) = (Vec::new(), Vec::new());
    parse(input, &mut l1, &mut l2);

    let mut cache = std::collections::HashMap::new();
    l1.iter()
        .map(|x| {
            if let Some(&v) = cache.get(x) {
                v
            } else {
                let n = l2.iter().filter(|&y| x == y).count();
                let v = x * n as i32;
                cache.insert(x, v);
                v
            }
        })
        .sum()
}

macro_rules! timeit {
    ($f:expr) => {{
        let now = std::time::Instant::now();
        let res = $f;
        (now.elapsed(), res)
    }};
}

fn main() {
    println!("part1 = {}", part1(INPUT));
    let (t1, r1) = timeit!(part2(INPUT));
    let (t2, r2) = timeit!(part2_with_cache(INPUT));
    assert_eq!(r1, r2);
    println!("part2 = {t1:?} part2_cache = {t2:?}");
}
