const TEST: &'static str = "3   4
4   3
2   5
1   3
3   9
3   3";

const INPUT: &'static str = include_str!("input");

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
    let mut sym = Vec::new();
    for &x in l1.iter() {
        let n = l2.iter().filter(|&&y| x == y).count();
        sym.push(x * n as i32);
    }

    sym.iter().sum()
}

fn main() {
    println!("part1 = {}", part1(INPUT));
    println!("part2 = {}", part2(INPUT));
}
