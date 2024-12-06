from rich import print
from time import time
from functools import cmp_to_key


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        elapsed = (time() - start) / 1000
        print(f"{fn.__name__} {elapsed=:.10f}ms {result=}")
        return result

    return wrapper


input = open("src/input").read().strip()

t1, t2 = [text.splitlines() for text in input.split("\n\n")]
order = [tuple(map(int, line.split("|"))) for line in t1]
updates = [tuple(map(int, line.split(","))) for line in t2]


@timeit
def part1():
    out = 0
    for u in updates:
        if not any(a in u and b in u and u.index(a) > u.index(b) for a, b in order):
            out += u[len(u) // 2]
    return out


@timeit
def part1_with_cache():
    cache = {}
    for x, y in order:
        cache[(x, y)] = True
        cache[(y, x)] = False

    out = 0
    for u in updates:
        if not any(k in cache and not cache[k] for k in zip(u, u[1:])):
            out += u[len(u) // 2]
    return out


@timeit
def part2():
    cache = {}
    for x, y in order:
        cache[(x, y)] = -1
        cache[(y, x)] = 1

    out = 0
    for u in updates:
        if any(cache.get(k, 0) == 1 for k in zip(u, u[1:])):
            cmp = cmp_to_key(lambda x, y: cache.get((x, y), 0))
            out += sorted(u, key=cmp)[len(u) // 2]
    return out


part1()
part1_with_cache()
part2()
