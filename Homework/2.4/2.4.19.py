def answer(num):
    m = 0
    for i in range(num):
        for j in range(num):
            m = max(m, len(str(min(i + 1, j + 1, num - i, num - j))))
    for i in range(num):
        for j in range(num):
            intermediate_value = min(i + 1, j + 1, num - i, num - j)
            print(" " * (m - len(str(intermediate_value))) + str(intermediate_value), end=" ")
        print()


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
