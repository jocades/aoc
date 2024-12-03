import re


input: str
with open("src/input") as f:
    input = f.read().strip()


def part1():
    # 161
    test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    out = 0
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input):
        out += int(m.group(1)) * int(m.group(2))
    return out


def part2():
    # 48
    test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    out = 0
    enabled = True
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\)|do\(\))", test):
        if m.group(3):
            enabled = m.group(3) == "do()"
        if enabled and m.group(1) and m.group(2):
            out += int(m.group(1)) * int(m.group(2))
        print(f"{out=} match={m.group(1, 2, 3)}")

    return out


print(part2())
