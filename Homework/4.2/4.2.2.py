def make_matrix(size, value=0):
    if type(size) is     tuple:
        return [[value for _ in range(size[0])] for _ in range(size[1])]
    return [[value for _ in range(size)] for _ in range(size)]


print(make_matrix(3))
