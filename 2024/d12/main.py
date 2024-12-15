from collections import deque
from time import time, sleep


input = open("input").read()

grid = input.splitlines()
rows = len(grid)
cols = len(grid[0])


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
seen = set()


def part1():
    def fence(r, c):
        q = deque([(r, c)])
        t = grid[r][c]
        count = 0
        sides = 0
        while len(q) > 0:
            cr, cc = q.popleft()
            count += 1
            seen.add((cr, cc))

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    sides += 1
                    continue

                if not grid[nr][nc] == t:
                    sides += 1
                    continue

                if (nr, nc) in seen:
                    continue

                if (nr, nc) not in q:
                    q.append((nr, nc))

        return count, sides

    fences = {}
    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            fences[(r, c)] = fence(r, c)

    out = sum(x * y for x, y in fences.values())
    print(out)
