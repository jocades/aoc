input = open(0).read()

g = input.splitlines()
rows = len(g)
cols = len(g[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1():
    def check(me, dir, t):
        i = 1
        while True:
            nr, nc = me[0] + dir[0] * i, me[1] + dir[1] * i
            if not (0 <= nr < rows and 0 <= nc < cols):
                break
            if int(g[nr][nc]) >= t:
                return False
            i += 1
        return True

    def rec(me, dir, t, i):
        nr, nc = me[0] + dir[0] * i, me[1] + dir[1] * i
        if not (0 <= nr < rows and 0 <= nc < cols):
            return True
        if int(g[nr][nc]) >= t:
            return False
        return rec(me, dir, t, i + 1)

    out = 2 * (rows + cols) - 4
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            t = int(g[r][c])
            for dir in dirs:
                if rec((r, c), dir, t, 1):
                    out += 1
                    break
    print(out)


def part2():
    from math import prod

    def rec(me, dir, t, i) -> int:
        nr, nc = me[0] + dir[0] * i, me[1] + dir[1] * i
        if not (0 <= nr < rows and 0 <= nc < cols):
            return i - 1
        if int(g[nr][nc]) >= t:
            return i
        return rec(me, dir, t, i + 1)

    out = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            t = int(g[r][c])
            score = prod(rec((r, c), dir, t, 1) for dir in dirs)
            if score > out:
                out = score
    print(out)


part2()
