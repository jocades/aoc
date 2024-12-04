const INPUT: &'static str = include_str!("input");

#[allow(dead_code)]
const TEST: &'static str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

fn parse_line(line: &str) -> Vec<i32> {
    line.split_whitespace()
        .map(|n| n.parse().unwrap())
        .collect()
}

fn is_safe(nums: &[i32]) -> bool {
    let mut v = nums.windows(2).all(|w| w[0] > w[1]) || nums.windows(2).all(|w| w[0] < w[1]);
    if v {
        for (a, b) in nums.iter().zip(&nums[1..]) {
            if !(1..=3).contains(&(a - b).abs()) {
                v = false;
                break;
            }
        }
    }
    v
}

fn part1(input: &str) -> usize {
    input
        .lines()
        .filter(|line| is_safe(&parse_line(line)))
        .count()
}

fn part2(input: &str) -> usize {
    input
        .lines()
        .filter(|line| {
            let nums = parse_line(line);
            (0..nums.len()).any(|i| is_safe(&[&nums[..i], &nums[i + 1..]].concat()))
        })
        .count()
}

fn main() {
    println!("part1 = {}", part1(INPUT));
    println!("part2 = {}", part2(INPUT));
}
