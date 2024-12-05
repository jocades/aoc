input = open("src/input").read()

test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""  # 18

grid = input.splitlines()

adjacent = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def part1():
    word = "XMAS"
    out = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == word[0]:
                for ar, ac in adjacent:
                    if not (
                        0 <= r + ar * len(word[1:]) < len(grid)
                        and 0 <= c + ac * len(word[1:]) < len(grid[0])
                    ):
                        continue

                    if all(
                        grid[r + ar * i][c + ac * i] == word[i]
                        for i in range(1, len(word))
                    ):
                        out += 1
    return out


def part2():
    word = "MAS"
    out = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] != word[1]:
                continue

            if "".join(
                grid[r + ar][c + ac]
                for ar, ac in [(-1, -1), (-1, 1), (1, 1), (1, -1)]
                # M . S
                # . A .
                # M . S
            ) in ["MSSM", "SSMM", "SMMS", "MMSS"]:
                out += 1
    return out


print(f"{part1()=}")
print(f"{part2()=}")
