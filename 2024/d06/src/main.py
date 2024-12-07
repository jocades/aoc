input = open("src/input").read().strip()

# list of chars since cannot set index in string
grid = [list(line) for line in input.splitlines()]
rows = len(grid)
cols = len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find():
    for r in range(rows):
        for c in range(cols):
            x = grid[r][c]
            if x != "." and x != "#":
                return r, c
    raise Exception("?")


def part1():
    r, c = find()
    d = 0

    seen = set()
    while True:
        seen.add((r, c))
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            break
        if grid[nr][nc] == "#":
            d = (d + 1) % 4
        else:
            r, c = nr, nc
    return len(seen)


def part2():
    r, c = find()

    def is_loop(grid: list[list[str]], r: int, c: int):
        d = 0
        dr, dc = dirs[d]
        seen = set()
        while True:
            if (r, c, dr, dc) in seen:
                return True
            seen.add((r, c, dr, dc))
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                return False
            if grid[nr][nc] == "#":
                d = (d + 1) % 4
                dr, dc = dirs[d]
            else:
                r, c = nr, nc

    out = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                continue
            grid[i][j] = "#"
            if is_loop(grid, r, c):
                out += 1
            grid[i][j] = "."
    return out


def part2_faster():
    r, c = find()

    def is_loop(grid: list[list[str]], r: int, c: int):
        d = 0
        dr, dc = dirs[d]
        seen = [False for _ in range(rows * cols * 4)]
        while True:
            key = (r * cols + c) * 4 + d
            if seen[key]:
                return True
            seen[key] = True

            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                return False
            if grid[nr][nc] == "#":
                d = (d + 1) % 4
                dr, dc = dirs[d]
            else:
                r, c = nr, nc

    out = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                continue
            grid[i][j] = "#"
            if is_loop(grid, r, c):
                out += 1
            grid[i][j] = "."
    return out


from time import time

start = time()
print(f"{part2()=} took {time() - start}s")

start = time()
print(f"{part2_faster()=} took {time() - start}s")
