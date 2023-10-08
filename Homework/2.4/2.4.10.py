def answer(num):
    print("А Б В")
    for i in range(1, num - 1):
        for j in range(1, num - i):
            print(i, j, num - i - j)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
