input = open(0).read()

size = 14


def ez():
    for i in range(len(input) - size + 1):
        diff = set(input[i : i + size])
        if len(diff) == size:
            print(i + size)
            break


def bit():
    def find(w):
        state = 0
        for c in w:
            prev = state
            state |= 1 << (ord(c) % 32)
            if state == prev:
                return False
        return True

    for i in range(len(input) - size + 1):
        window = input[i : i + size]
        if find(window):
            print(i + size)
            break


from time import time

s1 = time()
ez()
e1 = time() - s1

s2 = time()
bit()
e2 = time() - s2

print(f"ez took {e1:.6f}s")
print(f"bit took {e2:.6f}s")
