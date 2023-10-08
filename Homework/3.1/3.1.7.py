def answer(num1, num2):
    print(num1 + num2)


def main():
    num1, num2 = map(int, input().split())
    answer(num1, num2)


if __name__ == "__main__":
    main()
