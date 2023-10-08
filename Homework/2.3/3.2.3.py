def answer(a, b):
    for i in range(a, b + 1):
        print(i, end=" ")


def main():
    a = int(input())
    b = int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
