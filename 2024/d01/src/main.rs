const INPUT: &'static str = include_str!("input");

const TEST: &'static str = "3   4
4   3
2   5
1   3
3   9
3   3";

fn main() {
    let mut l1 = Vec::new();
    let mut l2 = Vec::new();

    for line in INPUT.lines() {
        let mut iter = line.split_whitespace();
        l1.push(iter.next().unwrap().parse::<i32>().unwrap());
        l2.push(iter.next().unwrap().parse::<i32>().unwrap());
    }

    l1.sort();
    l2.sort();

    let output: i32 = l1.iter().zip(&l2).map(|(&a, &b)| (a - b).abs()).sum();

    println!("{output}");
}
