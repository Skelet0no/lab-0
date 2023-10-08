def answer(a, b):
    num = 1
    for i in range(a):
        for j in range(b):
            print(" " * (len(str(a * b)) - len(str(num + (a * j)))) + str(num + (a * j)), end=" ")
        num += 1
        print()


def main():
    a, b = int(input()), int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
