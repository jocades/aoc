input: str
with open("src/input") as f:
    input = f.read().strip()

test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def is_safe(nums: list[int]) -> bool:
    v = all(a > b for a, b in zip(nums, nums[1:])) or all(
        a < b for a, b in zip(nums, nums[1:])
    )
    if v:
        for a, b in zip(nums, nums[1:]):
            if abs(a - b) not in range(1, 4):
                v = False
                break
    return v


out = 0
for line in input.split("\n"):
    nums = list(map(int, line.split()))
    if any(is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))):
        out += 1

print(out)
