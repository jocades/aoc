input = open("input").read().strip()


# a rock
# b paper
# c scissors

# a,a = 0
# a,b = -1
# a,c = 1

# b,a = 1
# b,b = 0
# b,c = -1

# c,a = -1
# c,b = 1
# c,c = 0


def part1():
    out = 0
    for line in input.splitlines():
        l, r = line.split()
        if r == "X":
            out += 1
            if l == "A":
                out += 3
            elif l == "C":
                out += 6
        elif r == "Y":
            out += 2
            if l == "A":
                out += 6
            elif l == "B":
                out += 3
        elif r == "Z":
            out += 3
            if l == "B":
                out += 6
            elif l == "C":
                out += 3
    print(out)


def part2():
    out = 0
    for line in input.splitlines():
        l, r = line.split()
        if r == "X":
            if l == "A":
                out += 3
            elif l == "B":
                out += 1
            elif l == "C":
                out += 2
        elif r == "Y":
            out += 3
            if l == "A":
                out += 1
            elif l == "B":
                out += 2
            elif l == "C":
                out += 3
        elif r == "Z":
            out += 6
            if l == "A":
                out += 2
            elif l == "B":
                out += 3
            elif l == "C":
                out += 1
    print(out)


part2()
