use std::{collections::HashSet, time::Duration};

const INPUT: &str = include_str!("input");

fn find(grid: &[Vec<char>]) -> Option<(usize, usize)> {
    for r in 0..grid.len() {
        for c in 0..grid[0].len() {
            let s = grid[r][c];
            if s != '.' && s != '#' {
                return Some((r, c));
            }
        }
    }
    None
}

const DIRS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

fn _part1(grid: &[Vec<char>]) -> usize {
    let rows = grid.len();
    let cols = grid[0].len();

    let (mut r, mut c) = find(&grid).unwrap();
    let mut d = 0;
    let (mut dr, mut dc) = DIRS[0];

    let mut seen = HashSet::new();
    loop {
        seen.insert((r, c));
        let nr = r as i32 + dr;
        let nc = c as i32 + dc;
        if !(0 <= nr && nr < rows as i32 && 0 <= nc && nc < cols as i32) {
            break;
        }
        if grid[nr as usize][nc as usize] == '#' {
            d = (d + 1) % 4;
            let pair = DIRS[d];
            dr = pair.0;
            dc = pair.1;
        } else {
            r = nr as usize;
            c = nc as usize;
        }
    }
    seen.len()
}

fn part2(grid: &mut [Vec<char>]) -> usize {
    let rows = grid.len();
    let cols = grid[0].len();

    let (r, c) = find(&grid).unwrap();

    let mut out = 0;
    for i in 0..rows {
        for j in 0..cols {
            if grid[i][j] != '.' {
                continue;
            }
            grid[i][j] = '#';
            let mut me = (r, c);
            let mut d = 0;
            let mut seen = HashSet::new();
            loop {
                seen.insert((me, DIRS[d]));
                let nr = me.0 as i32 + DIRS[d].0;
                let nc = me.1 as i32 + DIRS[d].1;

                if !(0 <= nr && nr < rows as i32 && 0 <= nc && nc < cols as i32) {
                    break;
                }
                if grid[nr as usize][nc as usize] == '#' {
                    d = (d + 1) % 4;
                } else {
                    me = (nr as usize, nc as usize);
                }
                if seen.contains(&(me, DIRS[d])) {
                    out += 1;
                    break;
                }
            }
            grid[i][j] = '.'
        }
    }
    out
}

fn part2_faster(g: &mut [Vec<char>]) -> usize {
    let rows = g.len();
    let cols = g[0].len();

    let me = find(&g).unwrap();

    fn is_loop(g: &[Vec<char>], mut me: (usize, usize)) -> bool {
        let rows = g.len();
        let cols = g[0].len();

        let mut d = 0;
        let mut seen = vec![false; rows * cols * 4];
        loop {
            let key = (me.0 * cols + me.1) * 4 + d;
            if seen[key] {
                return true;
            }
            seen[key] = true;

            let nr = me.0 as i32 + DIRS[d].0;
            let nc = me.1 as i32 + DIRS[d].1;
            if !(0 <= nr && nr < rows as i32 && 0 <= nc && nc < cols as i32) {
                return false;
            }
            if g[nr as usize][nc as usize] == '#' {
                d = (d + 1) % 4;
            } else {
                me = (nr as usize, nc as usize);
            }
        }
    }

    let mut out = 0;
    for i in 0..rows {
        for j in 0..cols {
            if g[i][j] == '.' {
                g[i][j] = '#';
                if is_loop(&g, me) {
                    out += 1;
                }
                g[i][j] = '.'
            }

            /* let mut me = (r, c);
            let mut d = 0;
            let mut seen = vec![false; rows * cols * 4];
            loop {
                let key = (me.0 * cols + me.1) * 4 + d;
                if seen[key] {
                    out += 1;
                    break;
                }
                seen[key] = true;

                let nr = me.0 as i32 + DIRS[d].0;
                let nc = me.1 as i32 + DIRS[d].1;
                if !(0 <= nr && nr < rows as i32 && 0 <= nc && nc < cols as i32) {
                    break;
                }
                if grid[nr as usize][nc as usize] == '#' {
                    d = (d + 1) % 4;
                } else {
                    me = (nr as usize, nc as usize);
                }
            } */
        }
    }
    out
}

macro_rules! timeit {
    ($f:expr) => {{
        let now = std::time::Instant::now();
        let res = $f;
        (now.elapsed(), res)
    }};
    ($f:expr,$n:expr) => {{
        let runs = (0..n).map(|_| $crate::timeit!($f));
        for _ in 0..n {
            runs.push($crate::timeit!($f))
        }
    }};
}

fn main() {
    let mut grid: Vec<Vec<char>> = INPUT.lines().map(|line| line.chars().collect()).collect();

    // println!("part1 = {}", part1(&grid));

    let (t2, r2) = timeit!(part2_faster(&mut grid));
    println!("part2_faster = {r2} took {t2:?}");

    /* let n = 5;
    let runs = (0..n)
        .map(|_| timeit!(part2_faster(&mut grid)).0)
        .collect::<Vec<_>>();

    #[derive(Debug, Default)]
    struct Stats {
        min: Duration,
        max: Duration,
        mean: Duration,
    }
    let mut stats = Stats::default();
    stats.max = runs[0];
    stats.min = runs[0];
    let mut sum = Duration::default();
    for &d in &runs[1..] {
        if d > stats.max {
            stats.max = d;
        }
        if d < stats.min {
            stats.min = d;
        }
        sum += d;
    }
    stats.mean = sum / (runs.len() - 1) as u32;

    println!("part2_faster = {r2} {stats:#?}"); */

    // let (t1, r1) = timeit!(part2(&mut grid));
    // assert_eq!(r1, r2);
    // println!("part2 = {r1} took {t1:?}");
}
