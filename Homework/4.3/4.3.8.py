def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        b, a = a + b, b


print(*fibonacci(10), sep=", ")
