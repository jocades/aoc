input = open(0).read()
# input = "R 10"

dirs = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}


# Chebyshev distance: d = max(x2 - x1, y2 - y1)
def distance(a: tuple[int, int], b: tuple[int, int]):
    return max(abs(b[0] - a[0]), abs(b[1] - a[1]))


def part1():
    hr, hc = 0, 0
    tr, tc = hr, hc
    seen = {(tr, tc)}

    for line in input.splitlines():
        d, s = line.split()
        for _ in range(int(s)):
            hr += dirs[d][0]
            hc += dirs[d][1]
            if max(abs(tr - hr), abs(tc - hc)) < 2:
                continue
            if tr < hr:
                tr += 1
            elif tr > hr:
                tr -= 1
            if tc < hc:
                tc += 1
            elif tc > hc:
                tc -= 1
            seen.add((tr, tc))

    print(len(seen))


def part2():
    from itertools import pairwise

    knots = [(0, 0) for _ in range(10)]
    seen = {(0, 0)}

    def move(i, a, b):
        r1, c1 = a
        r2, c2 = b
        if max(abs(r2 - r1), abs(c2 - c1)) < 2:
            return
        if r2 < r1:
            r2 += 1
        elif r2 > r1:
            r2 -= 1
        if c2 < c1:
            c2 += 1
        elif c2 > c1:
            c2 -= 1
        knots[i + 1] = (r2, c2)

    for line in input.splitlines():
        d, s = line.split()
        for _ in range(int(s)):
            knots[0] = (knots[0][0] + dirs[d][0], knots[0][1] + dirs[d][1])
            # for i, (a, b) in enumerate(zip(knots, knots[1:])):
            for i, (a, b) in enumerate(pairwise(knots)):
                move(i, a, b)
            seen.add(knots[-1])

    print(len(seen))


part2()
