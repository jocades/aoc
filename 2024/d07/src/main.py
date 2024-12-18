import re


input = open("input").read()


def solve(i, acc, t, nums):
    # print(i, acc, t, nums)
    if i == len(nums):
        return acc == t

    return (
        solve(i + 1, acc + nums[i], t, nums)
        or solve(i + 1, acc * nums[i], t, nums)
        or solve(i + 1, int(str(acc) + str(nums[i])), t, nums)
    )


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
