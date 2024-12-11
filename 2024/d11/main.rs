use std::collections::HashMap;

const INPUT: &str = include_str!("input");

type Cache = HashMap<(usize, u32), usize>;

fn count(n: usize, steps: u32, cache: &mut Cache) -> usize {
    if steps == 0 {
        return 1;
    }
    let k = (n, steps);
    if let Some(&result) = cache.get(&k) {
        println!("{n} {steps} {cache:?}");
        return result;
    }
    let result = match n {
        0 => count(1, steps - 1, cache),
        n => {
            let s = n.to_string();
            if s.len() % 2 == 0 {
                let (l, r) = s.split_at(s.len() / 2);
                count(l.parse().unwrap(), steps - 1, cache)
                    + count(r.parse().unwrap(), steps - 1, cache)
            } else {
                count(n * 2024, steps - 1, cache)
            }
        }
    };
    cache.insert(k, result);
    result
}

fn main() {
    let stones = INPUT
        .split_whitespace()
        .map(|n| n.parse::<usize>().unwrap())
        .collect::<Vec<_>>();
    println!("{stones:?}");

    let mut cache: Cache = HashMap::new();
    let out: usize = stones.iter().map(|&n| count(n, 25, &mut cache)).sum();
    println!("{out}");
}
