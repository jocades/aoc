const INPUT: &str = include_str!("input");

const _TEST: &str = "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX";

fn part1(grid: &[Vec<char>]) -> i32 {
    let word = ['X', 'M', 'A', 'S'];
    let mut out = 0;
    for r in 0..grid.len() {
        for c in 0..grid[0].len() {
            if grid[r][c] != word[0] {
                continue;
            }
            for ar in [-1, 0, 1] {
                for ac in [-1, 0, 1] {
                    if ar == 0 && ac == 0 {
                        continue;
                    }
                    let rest = word[1..].len() as isize;
                    let maxr = r as isize + ar * rest;
                    let maxc = c as isize + ac * rest;
                    if !((0 <= maxr && maxr < grid.len() as isize)
                        && (0 <= maxc && maxc < grid[0].len() as isize))
                    {
                        continue;
                    }
                    if (1..word.len()).all(|i| {
                        grid[(r as isize + ar * i as isize) as usize]
                            [(c as isize + ac * i as isize) as usize]
                            == word[i]
                    }) {
                        out += 1;
                    }
                }
            }
        }
    }
    out
}

fn part2(grid: &[Vec<char>]) -> i32 {
    let word = ['M', 'A', 'S'];
    let mut out = 0;
    for r in 1..grid.len() - 1 {
        for c in 1..grid[0].len() - 1 {
            if grid[r][c] != word[1] {
                continue;
            }

            let edges = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
                .map(|(ar, ac)| grid[(r as isize + ar) as usize][(c as isize + ac) as usize]);

            // M . S
            // . A .
            // M . S
            if [
                ['M', 'S', 'S', 'M'],
                ['S', 'S', 'M', 'M'],
                ['S', 'M', 'M', 'S'],
                ['M', 'M', 'S', 'S'],
            ]
            .iter()
            .any(|&pat| pat == edges)
            {
                out += 1;
            }
        }
    }
    out
}

fn main() {
    let grid: Vec<Vec<char>> = INPUT.lines().map(|line| line.chars().collect()).collect();
    println!("part1 = {}", part1(&grid));
    println!("part2 = {}", part2(&grid));
}
