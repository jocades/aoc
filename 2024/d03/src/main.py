import re

input: str
with open("src/input") as f:
    input = f.read().strip()

# 161
test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

out = 0
for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input):
    out += int(m.group(1)) * int(m.group(2))

print(out)
