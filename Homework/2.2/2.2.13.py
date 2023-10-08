def answer(num1, num2, num3):
    for i in "0123456789":
        if i in num1 and i in num2 and i in num3:
            return print(i)


def main():
    num1 = list(''.join(input()))
    num2 = list(''.join(input()))
    num3 = list(''.join(input()))
    answer(num1, num2, num3)


if __name__ == "__main__":
    main()
