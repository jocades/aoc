input = open("src/test").read().strip()

grid = input.splitlines()
rows = len(grid)
cols = len(grid[0])

dir = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
keys = list(dir.keys())


def find():
    for r in range(rows):
        for c in range(cols):
            s = grid[r][c]
            if s != "." and s != "#":
                return s, r, c
    raise Exception("?")


d, r, c = find()
dr, dc = dir[d]
print("start", r, c, d)

seen = set()
while True:
    print("current", r, c, grid[r][c])
    seen.add((r, c))

    # peek
    pr = r + dr
    pc = c + dc

    if not (0 <= pr < rows and 0 <= pc < cols):
        print("out of bounds!")
        break

    print("peek", pr, pc, grid[pr][pc])

    if grid[pr][pc] == "#":
        d = keys[(keys.index(d) + 1) % len(keys)]
        dr, dc = dir[d]
    else:
        r += dr
        c += dc


print(len(seen))
