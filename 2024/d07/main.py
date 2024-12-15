import re

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

input = open("input").read()


def solve(i, p, t, nums):
    if i == len(nums):
        if p == t:
            return True
        return False

    return solve(i + 1, p + nums[i], t, nums) or solve(i + 1, p * nums[i], t, nums)


out = 0
for line in input.splitlines():
    first, rest = line.split(":")
    total = int(first)
    nums = [int(n) for n in re.findall(r"\d+", rest)]

    if solve(1, nums[0], total, nums):
        out += total

print(out)

# line = "3267: 81 40 27"
# first, rest = line.split(":")
# total = int(first)
# nums = [int(n) for n in re.findall(r"\d+", rest)]
#
# print(solve(1, nums[0], total, nums))
