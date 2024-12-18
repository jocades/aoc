input = open(0).read()


g = input.splitlines()
rows = len(g)
cols = len(g[0])


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
seen = set()


def dfs(r: int, c: int, f: dict[str, int]):
    seen.add((r, c))
    f["count"] += 1

    def is_neighbour(dr, dc):
        nr, nc = r + dr, c + dc
        return 0 <= nr < rows and 0 <= nc < cols and g[nr][nc] == g[r][c]

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        # if not (0 <= nr < rows and 0 <= nc < cols) or g[r][c] != g[nr][nc]:
        if not is_neighbour(dr, dc):
            f["sides"] += 1
        elif (nr, nc) not in seen:
            dfs(nr, nc, f)


def dfs2(r: int, c: int, f: dict[str, int]):
    seen.add((r, c))
    f["count"] += 1

    def is_neighbour(dr, dc):
        nr, nc = r + dr, c + dc
        return 0 <= nr < rows and 0 <= nc < cols and g[nr][nc] == g[r][c]

    for d in range(4):
        dr, dc = dirs[d]
        ndr, ndc = dirs[(d + 1) % 4]

        if not is_neighbour(dr, dc) and not is_neighbour(ndr, ndc):
            f["sides"] += 1

        if (
            is_neighbour(dr, dc)
            and is_neighbour(ndr, ndc)
            and not is_neighbour(dr + ndr, dc + ndc)
        ):
            f["sides"] += 1

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if is_neighbour(dr, dc) and (nr, nc) not in seen:
            dfs2(nr, nc, f)


out = 0
for r in range(rows):
    for c in range(cols):
        if (r, c) not in seen:
            fence = dict(count=0, sides=0)
            # dfs(r, c, fence)
            dfs2(r, c, fence)
            out += fence["count"] * fence["sides"]
            print((r, c), fence)

print(out)
