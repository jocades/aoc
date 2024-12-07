#![allow(unused)]

struct Grid<T> {
    grid: Vec<Vec<T>>,
    rows: usize,
    cols: usize,
    node: Option<T>,
}

impl<T> Grid<T> {
    fn new(grid: Vec<Vec<T>>) -> Self {
        let rows = grid.len();
        // todo: check all cols
        let cols = grid[0].len();
        Self {
            grid,
            rows,
            cols,
            node: None,
        }
    }

    fn get(r: isize, c: isize) {}
}
