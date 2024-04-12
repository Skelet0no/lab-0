def cycle(inp):
    k = 0
    while True:
        yield inp[k % len(inp)]
        k += 1


print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
