input: str
with open("src/input") as f:
    input = f.read().strip()


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


output = 0
for line in input.split("\n"):
    nums = list(map(int, line.split()))
    if is_safe(nums) or any(
        is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))
    ):
        output += 1

print(output)
