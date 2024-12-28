input = open(0).read().strip()


# part1
elfs = []
for stack in input.split("\n\n"):
    elfs.append(sum(int(n) for n in stack.splitlines()))
print(max(elfs))

# oneliner:
out = max(sum(int(n) for n in elf.splitlines()) for elf in input.split("\n\n"))
print(out)


# part2
print(sum(sorted(elfs, reverse=True)[:3]))
