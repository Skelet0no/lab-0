def answer(a, b):
    num = 1
    for i in range(1, a + 1):
        if (i + 1) % 2 == 0:
            for j in range(1, b + 1):
                print(" " * (len(str(a * b)) - len(str(num))) + str(num), end=" ")
                num += 1
        else:
            for j in range(1, b + 1):
                print(" " * (len(str(a * b)) - len(str(num + b - j))) + str(num + b - j), end=" ")
            num += b
        print()


def main():
    a, b = int(input()), int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
