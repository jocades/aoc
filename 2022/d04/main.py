input = open(0).read()


def part1():
    out = 0
    for line in input.splitlines():
        a, b = line.split(",")
        amin, amax = map(int, a.split("-"))
        bmin, bmax = map(int, b.split("-"))
        if amin >= bmin and amax <= bmax or bmin >= amin and bmax <= amax:
            out += 1
    print(out)


def part2():
    out = 0
    for line in input.splitlines():
        a, b = line.split(",")
        amin, amax = map(int, a.split("-"))
        bmin, bmax = map(int, b.split("-"))
        if (
            bmin <= amin <= bmax
            or bmin <= amax <= bmax
            or amin <= bmin <= amax
            or amin <= bmax <= amax
        ):
            out += 1

    print(out)


part2()
