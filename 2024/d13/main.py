import re

input = open("input").read().strip()

""" blocks = []
for block in input.split("\n\n"):

    block = {}
    for line in block.splitlines():
        # block['a'] = ()
        blocks.appen """

test = """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176"""

blocks = []


# block = {}
for line in test.splitlines():
    matches = re.findall(r"Button.([A-Z]).*(\d+).*(\d+)", line)
    print(matches)
