input = open(0).read().strip()


# part 1
# out = 0
# for line in input.splitlines():
#     a, b = line[: len(line) // 2], line[len(line) // 2 :]
#     for c in set(c for c in a if c in b):
#         out += ord(c) % 32
#         if c.isupper():
#             out += 26


lines = input.splitlines()
size = 3

out = 0
for i in range(0, len(lines), size):
    a, b, c = lines[i : i + size]
    for char in set(char for char in a if char in b and char in c):
        out += ord(char) % 32
        if char.isupper():
            out += 26
print(out)
