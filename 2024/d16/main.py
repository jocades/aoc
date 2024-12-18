g = open(0).read().splitlines()
rows = len(g)
cols = len(g[0])


seen = set()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(r, c):
    if g[r][c] == "S":
        return True

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if g[nr][nc] == "#":
            dfs(nr, nc)
        else:
            pass


for r in range(rows):
    for c in range(cols):
        if g[r][c] == "S":
            print("start", (r, c))
            cr, cc = r, c
            d = 0
            last = (cr, cc, d)
            turns = 0
            while True:
                print("current", (cr, cc))

                if (cr, cc) in seen:
                    print("seen", (cr, cc))
                    # d =
                seen.add((cr, cc))

                dr, dc = dirs[d]
                nr, nc = cr + dr, cc + dc
                print("next", (nr, nc))

                if g[nr][nc] == "#":
                    if turns == 3:
                        lr, lc, ld = last
                        cr, cc = lr, lc
                        d = ld
                        continue

                    d = (d + 1) % 4
                    turns += 1
                    break
                else:
                    cr, cc = nr, nc

            print("end", (cr, cc), d, dirs[d])
