def answer(num):
    minimum = min(num % 10 + num // 10 % 10, num // 100 + num // 10 % 10)
    maximum = max(num % 10 + num // 10 % 10, num // 100 + num // 10 % 10)
    print(str(maximum) + str(minimum))


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
