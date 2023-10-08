def answer(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(i * j, end=" ")
        print()


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()