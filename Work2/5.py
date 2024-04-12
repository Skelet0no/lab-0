def grasshopper(start, finish, length):
    def bl(step, depth):
        if step == finish and depth == length:
            return [[step]]
        elif depth == length:
            return []

        ans = bl(step + 1, depth + 1) + bl(step - 1, depth + 1) + bl(step + 2, depth + 1) + bl(step - 2, depth + 1)
        return [[step] + i for i in ans]

    res = bl(start, 0)
    return res


print(*grasshopper(1, 10, 5), sep="\n")
print(*grasshopper(2, 5, 3), sep="\n")
