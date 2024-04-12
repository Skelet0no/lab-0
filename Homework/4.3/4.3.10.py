def make_linear(inp):
    for i in range(len(inp)):
        if type(inp[i]) is list:
            return make_linear(inp[:i]) + make_linear(inp[i]) + make_linear(inp[i + 1:])
    return inp


result = make_linear([1, [2, [3, 4]], 5, 6, [7, 8, [9]]])
print(result)
