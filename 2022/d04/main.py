input = open(0).read()

out = 0
for line in input.splitlines():
    a, b = line.split(",")
    amin, amax = [int(n) for n in a.split("-")]
    bmin, bmax = [int(n) for n in b.split("-")]
    if amin >= bmin and amax <= bmax or bmin >= amin and bmax <= amax:
        out += 1
print(out)
