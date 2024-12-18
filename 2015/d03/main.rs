const INPUT: &str = include_str!("input");

fn main() {
    let (mut r, mut c) = (0, 0);
    let mut seen = std::collections::HashSet::new();

    for ch in INPUT.chars() {
        match ch {
            '^' => r -= 1,
            '>' => c += 1,
            'v' => r += 1,
            '<' => c -= 1,
            _ => {}
        };
        seen.insert((r, c));
    }

    println!("{}", seen.len() + 1);
}
