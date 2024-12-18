const INPUT: &str = include_str!("input");

fn solve(i: usize, acc: u64, target: u64, nums: &[u64]) -> bool {
    if i == nums.len() {
        return acc == target;
    }

    solve(i + 1, acc + nums[i], target, nums)
        || solve(i + 1, acc * nums[i], target, nums)
        || solve(
            i + 1,
            (acc.to_string() + &nums[i].to_string()).parse().unwrap(),
            target,
            nums,
        )
}

fn main() {
    let mut out = 0;
    for line in INPUT.lines() {
        let (first, rest) = line.split_once(":").unwrap();
        let total: u64 = first.parse().unwrap();
        let nums: Vec<u64> = rest
            .split_whitespace()
            .map(|n| n.parse().unwrap())
            .collect();

        if solve(1, nums[0], total, &nums) {
            out += total;
        }
    }

    println!("{out}");
}
