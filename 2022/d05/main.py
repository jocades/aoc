import re

input = open(0).read()

puzzle, moves = input.split("\n\n")
n_crates = int(puzzle[-1].split()[-1])
crates = [[] for _ in range(n_crates)]

size = 4

for line in puzzle.splitlines()[:-1]:
    for i in range(0, len(line), size):
        crate = line[i : i + size].strip()
        if crate:
            crates[i // size].append(crate[1])

for stack in crates:
    stack.reverse()


def part1(count: int, src: int, dst: int):
    for _ in range(count):
        crates[dst - 1].append(crates[src - 1].pop())


def part2(count: int, src: int, dst: int):
    ls = [crates[src - 1].pop() for _ in range(count)]
    ls.reverse()
    crates[dst - 1] = crates[dst - 1] + ls


for move in moves.splitlines():
    for match in re.finditer(r"move (\d+) from (\d+) to (\d+)", move):
        count, src, dst = map(int, match.groups())
        # part1(count, src, dst)
        part2(count, src, dst)

out = "".join(stack.pop() for stack in crates)
print(out)
