def answer(a, b):
    if b > a:
        for i in range(a, b + 1):
            print(i, end=" ")
    else:
        for i in range(a, b - 1, -1):
            print(i, end=" ")


def main():
    a = int(input())
    b = int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
