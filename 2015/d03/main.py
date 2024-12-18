text = input()


r, c = 0, 0


seen = set()
for d in text:
    if d == "^":
        r -= 1
    elif d == ">":
        c += 1
    elif d == "v":
        r += 1
    elif d == "<":
        c -= 1

    seen.add((r, c))


print(len(seen) + 1)
