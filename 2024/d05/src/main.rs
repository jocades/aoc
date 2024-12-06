use std::collections::HashMap;

const INPUT: &str = include_str!("input");

fn part1() -> i32 {
    let (order, updates) = INPUT.split_once("\n\n").unwrap();

    let mut cache = HashMap::new();
    for line in order.lines() {
        let (x, y) = line
            .split_once("|")
            .map(|(x, y)| (x.parse::<i32>().unwrap(), y.parse::<i32>().unwrap()))
            .unwrap();
        cache.insert((x, y), true);
        cache.insert((y, x), false);
    }

    let mut out = 0;
    for line in updates.lines() {
        let u: Vec<i32> = line.split(",").map(|n| n.parse().unwrap()).collect();
        if !u
            .windows(2)
            .any(|w| cache.get(&(w[0], w[1])).is_some_and(|v| !v))
        {
            out += u[u.len() / 2];
        }
    }
    out
}

fn part2() -> i32 {
    let (order, updates) = INPUT.split_once("\n\n").unwrap();

    let mut cache = HashMap::new();
    for line in order.lines() {
        let (x, y) = line
            .split_once("|")
            .map(|(x, y)| (x.parse::<i32>().unwrap(), y.parse::<i32>().unwrap()))
            .unwrap();
        cache.insert((x, y), -1);
        cache.insert((y, x), 1);
    }

    let mut out = 0;
    for line in updates.lines() {
        let mut u: Vec<i32> = line.split(",").map(|n| n.parse().unwrap()).collect();
        if u.windows(2)
            .any(|w| cache.get(&(w[0], w[1])).is_some_and(|&v| v == 1))
        {
            u.sort_by(|&x, &y| cache.get(&(x, y)).unwrap_or(&0).cmp(&0));
            out += u[u.len() / 2];
        }
    }
    out
}

fn main() {
    println!("part1 = {}", part1());
    println!("part2 = {}", part2());
}
