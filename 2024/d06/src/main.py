input = open("src/input").read().strip()

grid = input.splitlines()
dir = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
keys = list(dir.keys())


def find():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            s = grid[r][c]
            if s != "." and s != "#":
                return s, r, c
    raise Exception("?")


d, r, c = find()
dr, dc = dir[d]
print("start", r, c, d)

out = []
while True:
    out.append((r, c))
    r += dr
    c += dc
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        print("out of bounds!")
        break

    if grid[r][c] == "#":
        print("touch", r, c)

        cr = r - dr
        cc = c - dc
        print("current", cr, cc)

        nd = keys[(keys.index(d) + 1) % len(keys)]
        nr, nc = dir[nd]
        r = cr + nr
        c = cc + nc
        print("next", nd, r, c)

        d = nd
        dr = nr
        dc = nc


print(len(set(out)))
