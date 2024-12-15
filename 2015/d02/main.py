from math import prod


input = open("input").read().splitlines()

out = 0
for line in input:
    nums = [int(n) for n in line.split("x")]
    nums.sort(reverse=True)
    out += sum(n * 2 for n in nums[1:]) + prod(nums)

    # part1:
    # dims = [l * w, w * h, h * l]
    # out += sum(2 * n for n in dims) + min(dims)


print(out)
